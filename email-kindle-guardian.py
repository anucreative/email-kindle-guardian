#!/bin/py
from urllib2 import Request, urlopen, HTTPError, URLError
from mailer import Mailer, Message
import datetime

# Change these vales to something particular to you
fromEmail = "me@authorisesender.com"
kindleEmail = "me@free.kindle.com"

def emailKindleGuardian(fromEmail, kindleEmail):
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
        message = Message(From=fromEmail, To=[kindleEmail], Subject="Guardian " + fileName)
        message.attach("/tmp/" + fileName)
        sender = Mailer("localhost")
        sender.send(message)

    except HTTPError, e:
        print e.code, url
    except URLError, e:
        print e.code, url


emailKindleGuardian(fromEmail, kindleEmail)

