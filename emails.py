"""Function to send emails to a list of recipients using SendInBlue SMTP API and python's SMTP library."""
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

import requests
from dotenv import load_dotenv

from otp import generate_otp
from util import is_variable_none

load_dotenv()

API_KEY = os.getenv("API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_NAME = os.getenv("SENDER_NAME")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SUBJECT = os.getenv("SUBJECT")
URL = os.getenv("URL")

required_variables = [
    API_KEY,
    SENDER_EMAIL,
    SENDER_NAME,
    SENDER_PASSWORD,
    SMTP_SERVER,
    SMTP_PORT,
    SUBJECT,
    URL,
]
if is_variable_none(required_variables):
    raise ValueError("One or more env variables are missing.")


def generate_content(code: str):
    """
    The function generates an email content with a unique OTP code for a registered user for the
    upcoming 2023 COMPSSA elections.

    Args:
      code: The OTP code that will be generated and inserted into the email content.

    Returns:
      an HTML formatted string that includes a greeting, a message thanking the recipient for
    registering for an election, and an OTP code that the recipient will need for the voting form.
    """
    return f"""<p>Hello,<br>
Hope you are good.
<br>
<p>Thank you for registering for the upcoming 2023 COMPSSA elections.<br>
Below is your OTP code. You'll need this for the voting form.<br>
Your otp code is <p style='font-size:16px; font-weight:bold;'>{code}<br></p><p>Thank you.</p>
"""


def send_email_via_send_in_blue(recipient_emails: List[str]):
    student_code = []
    # Define the email message payload
    for email in recipient_emails:
        code = generate_otp()
        student_code.append(code)

        payload = {
            "sender": {"name": SENDER_NAME, "email": SENDER_EMAIL},
            "to": [{"email": email}],
            "subject": SUBJECT,
            "htmlContent": generate_content(code),
        }
        # Define the API headers and authentication
        headers = {"Content-Type": "application/json", "api-key": API_KEY}

        # Send the email using the Sendinblue API
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        if response.status_code != 201:
            print(f"Error sending email to {email}, {response.text}")
        else:
            print(f"Successfully sent email to {email}")

    # Check the response status code
    if response.status_code == 201:
        print("Emails sent successfully.")
    return student_code


def send_bulk_email(recipients: List[str]):
    """
    The function sends bulk emails to a list of recipients and returns a list of generated codes for
    each recipient.

    Args:
      recipients (List[str]): A list of email addresses to which the bulk email will be sent.

    Returns:
      a list of student codes generated for each recipient in the input list.
    """
    student_code = []

    # Log in to the SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    # Send the email to each recipient in the list
    for recipient in recipients:
        code = generate_otp()
        student_code.append(code)

        message = generate_content(code)

        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = SUBJECT
        msg.attach(MIMEText(message, "html"))

        server.sendmail(SENDER_EMAIL, recipient, msg.as_string())

    # Close the SMTP server connection
    server.quit()
    return student_code


def send_single_email(recipient: str):
    """
    This function sends a single email with a generated one-time password to a specified recipient.

    Args:
      recipient (str): The email address of the recipient to whom the email will be sent.

    Returns:
      the generated OTP code.
    """
    # Log in to the SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    # Send the email to each recipient in the list
    code = generate_otp()

    message = generate_content(code)

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient
    msg["Subject"] = SUBJECT
    msg.attach(MIMEText(message, "html"))

    server.sendmail(SENDER_EMAIL, recipient, msg.as_string())

    # Close the SMTP server connection
    server.quit()
    return code


print("yaw")
