import smtplib
# set up the SMTP server


def sendMail(recipient, title, message):
    EMAIL_ADDRESS = "karickopro@gmail.com"
    EMAIL_PASSWORD = "0923204647na"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    msg = """\
Subject: {}

{}""".format(title, message)

    server.sendmail(EMAIL_ADDRESS, recipient, msg)
