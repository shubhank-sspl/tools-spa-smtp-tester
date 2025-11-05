# 📧 Feature-Rich SMTP Configuration Tester (Streamlit + Python)

A simple, powerful, single-page web application built with Streamlit and Python's `smtplib` library to test your SMTP server settings, authentication, and encryption protocols (SSL/TLS, STARTTLS).



## ✨ Features

* **Flexible Encryption:** Test connections using Plain SMTP, STARTTLS (Port 587), or SSL/TLS (Port 465).
* **Robust Error Handling:** Provides clear, user-friendly error messages for common issues like authentication failure (`SMTPAuthenticationError`) or connection refusal (`SMTPConnectError`).
* **Connection Timeout:** Specify a custom timeout value to prevent long waits.
* **Single-Form Workflow:** All inputs are contained within a single Streamlit form, ensuring the test runs only after the "Test" button is pressed.

## 🚀 Deployment & Local Setup

This application is ready for one-click deployment to [Streamlit Community Cloud](https://streamlit.io/cloud).

### Local Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/smtp-tester-app.git](https://github.com/YOUR_USERNAME/smtp-tester-app.git)
    cd smtp-tester-app
    ```
2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    The necessary libraries are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    streamlit run smtp_tester.py
    ```
    The app will automatically open in your web browser.

## 💡 Usage Notes (Important!)

When testing commercial email providers like **Gmail** or **Outlook**, you must typically use an **App Password** instead of your main account password.

* **Gmail:** Requires 2-Factor Authentication to be enabled. Generate an App Password in your Google Account security settings.
* **Outlook/Office 365:** Requires modern authentication/app passwords.

---
