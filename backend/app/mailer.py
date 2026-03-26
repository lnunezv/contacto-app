import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM = os.getenv("SMTP_FROM")
SMTP_TO = os.getenv("SMTP_TO")


def send_contact_email(name, email, subject, message):
    body = f"""
Nuevo contacto recibido:

Nombre: {name}
Email: {email}
Asunto: {subject}
Mensaje: {message}
"""

    msg = MIMEText(body)
    msg["Subject"] = f"Nuevo contacto: {subject}"
    msg["From"] = SMTP_FROM
    msg["To"] = SMTP_TO

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_FROM, SMTP_TO, msg.as_string())