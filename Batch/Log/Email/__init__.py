import smtplib
from email.mime.text import MIMEText


class EmailSender:

    def __init__(self):
        session = smtplib.SMTP('smtp.live.com', 587)

        session.starttls()

        smpt.login("")

        pass

