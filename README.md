# Email Kindle Guardian
This is a simple node.js programme to download the day's .mobi copy of the Guardian from mythic-beasts.com ([Mark Longair](http://mythic-beasts.com/~mark/random/guardian-for-kindle/) did most of the work) and send it to a Kindle email address.

Built and tested with node 0.6, 0.8.

It's run as a node-cron job to send you a copy of the paper each morning. I have mine to send to run at 05:00. Don't set it to run too early - I'm not sure when Mark's download is available each day...

## Set up
###Install the following packages (using npm install):

* [nodemailer](http://andris9.github.com/Nodemailer/)
* [moment](http://momentjs.com/)
* [cron](https://github.com/ncb000gt/node-cron)

These packages should be installed already:

* fs
* url
* http

###Sensitive info (such as email addresses) are stored in heroku .env

	heroku config:add KINDLE_EMAIL_ADDRESS=Your Kindle email address GMAIL_ADDRESS=Your Gmail address GMAIL_PASSWORD=Your Gmail password

###Run it:

	node app.js