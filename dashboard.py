from email_sender import send_email
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os


st.title("📧 Email Automation System")


uploaded_file = st.file_uploader(
    "Upload Student CSV",
    type="csv"
)


if uploaded_file is not None:

    students = pd.read_csv(uploaded_file)

    st.success("CSV uploaded successfully!")

    st.dataframe(students)


    subject = st.text_input(
        "Email Subject"
    )


    message = st.text_area(
        "Email Message"
    )


    st.write("Preview:")

    if len(students) > 0:

        name = students.iloc[0]["name"]

        preview = message.replace(
            "{name}",
            name
        )

        st.info(preview)
        load_dotenv()
    sender_email = os.getenv("EMAIL")
    app_password = os.getenv("APP_PASSWORD")


    if st.button("Send Emails"):

        for index, row in students.iterrows():

            name = row["name"]
            email = row["email"]

            personalized_message = message.replace(
                "{name}",
                name
            )

            try:

                send_email(
                  sender_email,
                  app_password,
                  email,
                  subject,
                  personalized_message
                  )

                st.success(
                    f"Email sent to {name}"
                )


            except Exception as e:
                   st.error(f"Failed for {name}: {e}")