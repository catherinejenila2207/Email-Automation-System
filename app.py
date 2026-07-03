import pandas as pd
from email_sender import send_email
from datetime import datetime
import csv
from dotenv import load_dotenv
import os



students = pd.read_csv("students.csv")
load_dotenv()

sender_email = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")

with open("email_log.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Email", "Status", "Time"])


    for index, row in students.iterrows():

        name = row["name"]
        email = row["email"]

        try:

            send_email(
                sender_email,
                app_password,
                email,
                name
            )

            status = "Sent"


        except Exception as e:

            status = "Failed"


        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        writer.writerow(
            [name, email, status, time]
        )


        print(name, status)