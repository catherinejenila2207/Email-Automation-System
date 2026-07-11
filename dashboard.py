import streamlit as st
import pandas as pd
from email_sender import send_email
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

sender_email = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")

st.set_page_config(page_title="Email Automation System", page_icon="📧")

st.title("📧 Email Automation System")

uploaded_file = st.file_uploader(
    "Upload Student CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        students = pd.read_csv(uploaded_file)

        st.success("✅ CSV uploaded successfully")

        st.dataframe(students)

        # Check required columns
        if "name" not in students.columns or "email" not in students.columns:
            st.error("CSV must contain 'name' and 'email' columns.")
            st.stop()

        subject = st.text_input(
            "Email Subject",
            value="Welcome"
        )

        message = st.text_area(
            "Email Message",
            value="""Hello {name},

Welcome!

This email was sent using my Email Automation System.

Regards,
Catherine Jenila"""
        )

        st.subheader("Preview")

        preview = message.replace(
            "{name}",
            students.iloc[0]["name"]
        )

        st.info(preview)

        if st.button("📨 Send Emails"):

            if not sender_email or not app_password:
                st.error("EMAIL or APP_PASSWORD is missing.")
                st.stop()

            progress = st.progress(0)

            total = len(students)

            for i, row in students.iterrows():

                try:

                    personalized_message = message.replace(
                        "{name}",
                        row["name"]
                    )

                    send_email(
                        sender_email,
                        app_password,
                        row["email"],
                        subject,
                        personalized_message
                    )

                    st.success(f"✅ Email sent to {row['name']}")

                except Exception as e:

                    st.error(f"❌ Failed for {row['name']}: {e}")

                progress.progress((i + 1) / total)

            st.balloons()
            st.success("🎉 All emails processed!")

    except Exception as e:
        st.error(f"Error reading CSV: {e}")