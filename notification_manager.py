# This class is responsible for sending notifications with the deal flight details.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class NotificationManager:
    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password

    def send_email(self, receiver_email='heykashif@gmail.com', subject='', body=''):
        # Create the email message
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = 'heykashif@gmail.com'
        message["Subject"] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server (in this case, Gmail)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, 'heykashif@gmail.com', message.as_string())



