import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject: str, body: str):
    msg = MIMEMultipart()
    msg["From"] = os.environ["EMAIL_ADDRESS"]
    msg["To"] = os.environ["EMAIL_TO"]
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.environ["EMAIL_ADDRESS"],
            os.environ["EMAIL_PASSWORD"],
        )
        server.send_message(msg)
