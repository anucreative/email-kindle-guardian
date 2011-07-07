#!/usr/bin/python
from urllib2 import Request, urlopen, HTTPError, URLError
from mailer import Mailer, Message
from ConfigParser import ConfigParser
import datetime

def setup():
    config = ConfigParser()
    config.readfp(open("config.ini"))
    settings = {}
    settings['fromEmail'] = config.get("EmailKindleGuardian","FromEmail")
    settings['kindleEmail'] = config.get("EmailKindleGuardian","KindleEmail")
    return settings

def emailKindleGuardian():
    settings = setup()
    now = datetime.datetime.now()
    fileName = "gdn-" + format(now.year, "02d") + "-" + format(now.month, "02d") + "-" + format(now.day, "02d") + ".mobi"
    url = "http://mythic-beasts.com/~mark/random/guardian-for-kindle/" + fileName
    # Download the file!
    req = Request(url)
    try:
        f = urlopen(req)
        print "Downloading " + url
        # Download the file to tmp
        localFile = open("/tmp/" + fileName, "w+")
        localFile.write(f.read())
        localFile.close()
        # Yey!, we've downloaded the file. Email it!
        message = Message(From=settings['fromEmail'], To=[settings['kindleEmail']], Subject="Guardian " + fileName)
        message.attach("/tmp/" + fileName)
        sender = Mailer("localhost")
        sender.send(message)
        print "Yey! I've sent today's Guardian to " + settings['kindleEmail']

    except HTTPError, e:
        print e.code, url
    except URLError, e:
        print e.code, url


emailKindleGuardian()

