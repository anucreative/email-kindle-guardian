# Email Kindle Guardian
This is a simple python programme to download they day's *.mobi copy of the Guardian from mythic-beasts.com (Mark did most of the work: http://mythic-beasts.com/~mark/random/guardian-for-kindle/) and send it to a Kindle email address over email.

This programme is probably best run as a daily cron job to send you a copy of the paper each morning. I have mine to send at 08:00.

## Set up
This programme requires python Mailer which can be found at http://pypi.python.org/pypi/mailer

Clone the repo and change the fromEmail to an email address that is authorised to send Kindle books to your Kindle. Change kindleEmail to your Kindle's free or paid email account.
