#!/usr/bin/python
import datetime
import sys
from urllib2 import Request, urlopen, HTTPError, URLError
from ConfigParser import ConfigParser
from mailer import Mailer, Message

def setup():
    config = ConfigParser()
    with open(sys.path[0] + "/config.ini") as f:
        config.readfp(f)
    settings = {}
    try:
        settings['from_email'] = config.get("EmailKindleGuardian","from_email")
        settings['kindle_email'] = config.get("EmailKindleGuardian","kindle_email")
    except:
        raise SystemExit('buggered up')
        
    return settings


def email_kindle_guardian(from_email, kindle_email):
    now = datetime.datetime.now()
    file_name = "gdn-" + format(now.year, "02d") + "-" + format(now.month, "02d") + "-" + format(now.day, "02d") + ".mobi"
    url = "http://mythic-beasts.com/~mark/random/guardian-for-kindle/" + file_name
    # Download the file!
    req = Request(url)

    try:
        f = urlopen(req)
        print "Downloading " + url
        # Download the file to tmp
        with open("/tmp/" + file_name, "w+") as local_file:
            local_file.write(f.read())

        # Yey!, we've downloaded the file. Email it!
        message = Message(From=from_email, To=[kindle_email], Subject="Guardian " + file_name)
        message.attach("/tmp/" + file_name)
        sender = Mailer("localhost")
        sender.send(message)
        print "Yey! I've sent today's Guardian to " + kindle_email

    except HTTPError, e:
        print e.code, url

    except URLError, e:
        print e.code, url


if __name__ == '__main__':
    settings = setup()
    email_kindle_guardian(settings['from_email'], settings['kindle_email'])
