import streamlit as st
import pandas as pd
from email_sender import send_email

# Read secrets from Streamlit Cloud
sender_email = st.secrets["EMAIL"]
app_password = st.secrets["APP_PASSWORD"]

st.set_page_config(
    page_title="Email Automation System",
    page_icon="📧"
)

st.title("📧 Email Automation System")

uploaded_file = st.file_uploader(
    "Upload Student CSV",
    type=["csv"]
)

if uploaded_file:

    try:
        students = pd.read_csv(uploaded_file)

        if "name" not in students.columns or "email" not in students.columns:
            st.error("CSV must contain 'name' and 'email' columns.")
            st.stop()

        st.success("CSV Uploaded Successfully!")
        st.dataframe(students)

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
Catherine Jenila
"""
        )

        st.subheader("Preview")

        st.info(
            message.replace(
                "{name}",
                students.iloc[0]["name"]
            )
        )

        if st.button("📨 Send Emails"):

            progress = st.progress(0)

            total = len(students)

            for i, row in students.iterrows():

                personalized_message = message.replace(
                    "{name}",
                    row["name"]
                )

                try:

                    send_email(
                        sender_email,
                        app_password,
                        row["email"],
                        subject,
                        personalized_message
                    )

                    st.success(
                        f"✅ Email sent to {row['name']}"
                    )

                except Exception as e:

                    st.error(
                        f"❌ Failed for {row['name']}: {e}"
                    )

                progress.progress((i + 1) / total)

            st.balloons()
            st.success("🎉 All Emails Sent!")

    except Exception as e:
        st.error(e)