var

// Required modules
nodemailer = require("nodemailer"),
moment = require("moment"),
fs = require("fs"),
url = require("url"),
http = require("http"),
cronJob = require("cron").CronJob,
kindleEmail = process.env('KINDLE_EMAIL_ADDRESS'),
gmailAddress = process.env('GMAIL_ADDRESS'),
gmailPassword = process.env('GMAIL_PASSWORD'),


sendGuardian = function(filePath) {
    fs.readFile(filePath, function(err, data) {
        if (err) console.log(err);
        else {

            // Create reusable transport method (opens pool of SMTP connections)
            var smtpTransport = nodemailer.createTransport("SMTP",{
                service: "Gmail",
                auth: {
                    user: gmailAddress,
                    pass: gmailPassword
                }
            });

            // Setup e-mail data
            var mailOptions = {
                from: gmailAddress,
                to: kindleEmail,
                subject: "Guardian",
                attachments: [{
                    filename: filePath.split("/").pop(),
                    contents: data
                }]
            };

            // Send mail with defined transport object
            smtpTransport.sendMail(mailOptions, function(err, response){
                if (err) console.log(error);
                else {
                    console.log("Message sent: " + response.message);
                    // TODO: Remove .mobi file as we don"t need it anymore
                }

                // Shut down the connection pool, no more messages
                smtpTransport.close();
            });
        }
    });
},


downloadGuardian = function() {
    var
    now = new moment(),
    formattedDate,
    downloadDir = "./tmp/",
    fileName,
    fileUrl,
    options,
    file;
    
    formattedDate = now.format("YYYY-MM-DD");
    fileName = "gdn-" + formattedDate + ".mobi";
    fileUrl = "http://mythic-beasts.com/~mark/random/guardian-for-kindle/" + fileName;

    options = {
        host: url.parse(fileUrl).host,
        port: 80,
        path: url.parse(fileUrl).pathname
    };


    file = fs.createWriteStream(downloadDir + fileName);

    http.get(options, function(res) {
        res.on("data", function(data) {
            file.write(data);
        }).on("end", function() {
            file.end();
            console.log(fileName + " downloaded to " + downloadDir);
            sendGuardian(downloadDir + fileName);
        });
    });
},


job = new cronJob({
    cronTime: "00 00 5 * * *",
    onTick: function(){
        console.log("Wakey wakey, time to download the Guardian");
        downloadGuardian();
    },
    start: false
});


job.start();



