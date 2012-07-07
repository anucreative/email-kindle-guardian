# Email Kindle Guardian
This is a simple node programme to download they day's *.mobi copy of the Guardian from mythic-beasts.com (Mark did most of the work: http://mythic-beasts.com/~mark/random/guardian-for-kindle/) and send it to a Kindle email address over email.

Built and tested with node 0.6.

It's run as a node-cron job to send you a copy of the paper each morning. I have mine to send to run at 05:00.

## Set up
Requires:
- nodemailer
- moment
- fs
- url
- http
- cron

Create a config.js file with the following:
var config = {
	kindleEmail: "Your kindle email address",
	fromEmail: "Your GMail address",
	fromPassword: "Your GMail password"
};

module.exports = config;