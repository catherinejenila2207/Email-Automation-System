import pandas as pd
from email_sender import send_email
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")

students = pd.read_csv("students.csv")

subject = "Welcome"

for index, row in students.iterrows():

    name = row["name"]
    email = row["email"]

    message = f"""
Hello {name},

This is a test email sent from my Email Automation System.

Thank you.

Regards,
Catherine Jenila
"""

    try:
        send_email(
            sender_email,
            app_password,
            email,
            subject,
            message
        )

        print(f"{name} : Sent")

    except Exception as e:
        print(f"{name} : Failed - {e}")