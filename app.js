var nodemailer = require("nodemailer");
var moment = require("moment");
var fs = require("fs");
var url = require('url');
var http = require('http');
var cronJob = require('cron').CronJob;

var downloadDir = "./tmp/";
var formattedDate;


var sendGuardian = function(fileName) {
    fs.readFile(downloadDir + fileName, function(err, data) {
        if (err) {
            console.log(err);
            return;
        }

        // create reusable transport method (opens pool of SMTP connections)
        var smtpTransport = nodemailer.createTransport("SMTP",{
            service: "Gmail",
            auth: {
                user: "rob@anucreative.com",
                pass: "olsen570"
            }
        });

        // Setup e-mail data
        var mailOptions = {
            from: "Robert Douglas <rob@anucreative.com>",
            to: "anucreative@kindle.com",
            subject: "Guardian (" + formattedDate + ")",
            attachments: [{
                filename: fileName,
                contents: data
            }]
        };

        // send mail with defined transport object
        smtpTransport.sendMail(mailOptions, function(err, response){
            if (err) console.log(error);
            else {
                console.log("Message sent: " + response.message);
                // TODO: Remove .mobi file as we don't need it anymore
            }

            smtpTransport.close(); // shut down the connection pool, no more messages
        });
    });
};


var downloadGuardian = function() {
    var
    now = new moment(),
    fileName,
    fileUrl;
    
    formattedDate = now.format("YYYY-MM-DD");
    fileName = "gdn-" + formattedDate + ".mobi";
    fileUrl = "http://mythic-beasts.com/~mark/random/guardian-for-kindle/" + fileName;

    var options = {
        host: url.parse(fileUrl).host,
        port: 80,
        path: url.parse(fileUrl).pathname
    };


    var file = fs.createWriteStream(downloadDir + fileName);

    http.get(options, function(res) {
        res.on('data', function(data) {
            file.write(data);
        }).on('end', function() {
            file.end();
            console.log(fileName + ' downloaded to ' + downloadDir);
            sendGuardian(fileName);
        });
    });
};


var job = new cronJob({
    cronTime: '00 00 5 * * *',
    onTick: function(){
        console.log('Wakey wakey, time to download the Guardian');
        downloadGuardian();
    },
    start: false
});


job.start();



