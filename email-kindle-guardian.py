#!/usr/bin/python
import datetime
import sys
from urllib2 import Request, urlopen, HTTPError, URLError
from ConfigParser import ConfigParser
from mailer import Mailer, Message

def setup():
    config = ConfigParser()
    config.readfp(open(sys.path[0] + "/config.ini"))
    settings = {}
    settings['from_email'] = config.get("EmailKindleGuardian","FromEmail")
    settings['kindle_email'] = config.get("EmailKindleGuardian","KindleEmail")
    return settings

def email_kindle_guardian():
    settings = setup()
    now = datetime.datetime.now()
    file_name = "gdn-" + format(now.year, "02d") + "-" + format(now.month, "02d") + "-" + format(now.day, "02d") + ".mobi"
    url = "http://mythic-beasts.com/~mark/random/guardian-for-kindle/" + file_name
    # Download the file!
    req = Request(url)
    try:
        f = urlopen(req)
        print "Downloading " + url
        # Download the file to tmp
        local_file = open("/tmp/" + file_name, "w+")
        local_file.write(f.read())
        local_file.close()
        # Yey!, we've downloaded the file. Email it!
        message = Message(From=settings['from_email'], To=[settings['kindle_email']], Subject="Guardian " + file_name)
        message.attach("/tmp/" + file_name)
        sender = Mailer("localhost")
        sender.send(message)
        print "Yey! I've sent today's Guardian to " + settings['kindle_email']
    except HTTPError, e:
        print e.code, url
    except URLError, e:
        print e.code, url

email_kindle_guardian()

