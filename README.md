# 📧 Email Automation System

A web-based Email Automation System built using **Python**, **Streamlit**, **Pandas**, and **Gmail SMTP**. This application allows users to upload a CSV file containing recipient details and send personalized emails automatically.

---

## 🚀 Features

- 📂 Upload CSV file
- 📧 Send personalized emails
- 👤 Dynamic `{name}` placeholder replacement
- 📊 View uploaded student data
- 🔒 Secure email credentials using `.env`
- ⚠️ Error handling for failed emails
- 🖥️ Simple Streamlit web interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- SMTP (Gmail)
- python-dotenv
- Git & GitHub

---

## 📁 Project Structure

```
Email-Automation-System/
│
├── dashboard.py
├── email_sender.py
├── app.py
├── students.csv
├── requirements.txt
├── .gitignore
├── README.md
└── .env (not uploaded to GitHub)
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/catherinejenila2207/Email-Automation-System.git
```

Go to the project folder:

```bash
cd Email-Automation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run dashboard.py
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```
EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
```

> Never upload your `.env` file to GitHub.

---


## 👩‍💻 Author

**Catherine Jenila**

GitHub:
https://github.com/catherinejenila2207

---

## ⭐ Future Improvements

- Email attachments
- HTML email templates
- Scheduled email sending
- Multiple CSV formats
- Email analytics dashboard

---

## 📄 License

This project is created for learning and portfolio purposes.