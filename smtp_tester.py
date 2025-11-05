import streamlit as st
import smtplib
import ssl
from email.message import EmailMessage
import time

# --- Configuration ---
st.set_page_config(page_title="SMTP Tester", layout="wide")
st.title("📧 Feature-Rich SMTP Configuration Tester")

# Initialize a container for status messages
status_message = st.container()

# --- Core Function to Test SMTP Settings ---
def test_smtp(host, port, encryption, user, password, from_addr, to_addr, subject, body, timeout):
    """Attempts to connect, authenticate, and send an email."""
    try:
        # Create a basic email message
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr

        # Create a secure SSL context
        context = ssl.create_default_context()
        
        # --- Connection and Encryption Logic ---
        if encryption == "SSL/TLS (Port 465)":
            with smtplib.SMTP_SSL(host, port, context=context, timeout=timeout) as server:
                server.ehlo()
                server.login(user, password)
                server.send_message(msg)
                return "✅ Success: Test email sent successfully!"

        elif encryption == "STARTTLS (Port 587)":
            with smtplib.SMTP(host, port, timeout=timeout) as server:
                server.ehlo()
                server.starttls(context=context) # Upgrade to a secure connection
                server.ehlo()
                server.login(user, password)
                server.send_message(msg)
                return "✅ Success: Test email sent successfully after STARTTLS!"
                
        elif encryption == "Plain Text (Port 25/587)":
            # Note: Rarely recommended for real credentials without a secure path.
            with smtplib.SMTP(host, port, timeout=timeout) as server:
                server.ehlo()
                server.login(user, password)
                server.send_message(msg)
                return "✅ Success: Test email sent successfully over a plain-text connection."

    except smtplib.SMTPAuthenticationError:
        return "❌ Failure: Authentication failed. Check your username/password or app password settings."
    except smtplib.SMTPConnectError as e:
        return f"❌ Failure: Connection failed. Check host, port, or firewall. Error: {e}"
    except TimeoutError:
        return f"❌ Failure: Connection timed out after {timeout} seconds."
    except Exception as e:
        return f"❌ An unexpected error occurred: {e}"

# --- Streamlit UI: Form and Inputs ---

# Use st.form to batch inputs and only re-run on submission
with st.form("smtp_test_form", clear_on_submit=False):
    
    st.header("⚙️ Configuration")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Server Details")
        smtp_host = st.text_input("SMTP Server Host", value="smtp.example.com", key="host")
        smtp_port = st.number_input("Port", value=587, step=1, min_value=1, key="port")
        encryption_type = st.selectbox(
            "Encryption Method",
            ["STARTTLS (Port 587)", "SSL/TLS (Port 465)", "Plain Text (Port 25/587)"],
            index=0, key="encryption"
        )
        timeout_sec = st.number_input("Connection Timeout (seconds)", value=10, step=1, min_value=1, max_value=60, key="timeout")

    with col2:
        st.subheader("Login Credentials")
        smtp_user = st.text_input("Sender Email (Username)", value="test@example.com", key="user")
        smtp_password = st.text_input("Password / App Password", type="password", key="password")

    st.markdown("---")
    st.header("✉️ Email Content")
    col3, col4 = st.columns(2)
    
    with col3:
        sender_email = st.text_input("From Email Address", value="test@example.com", key="from_addr")
    with col4:
        recipient_email = st.text_input("Recipient Email Address", value="receiver@example.com", key="to_addr")
    
    email_subject = st.text_input("Subject", value="SMTP Test from Streamlit", key="subject")
    email_body = st.text_area("Email Body (Plain Text)", value="This is a test email to verify your SMTP configuration.", key="body")
    
    st.markdown("---")
    
    # Form Submit Button
    submitted = st.form_submit_button("🚀 Test SMTP Connection and Send Email")

# --- Execution Logic (Outside the form) ---

if submitted:
    # Basic input validation
    if not all([smtp_host, smtp_port, smtp_user, smtp_password, sender_email, recipient_email]):
        status_message.error("Please fill in all required configuration and email fields.")
    else:
        with status_message:
            # Display a spinner while the test is running
            with st.spinner('Testing SMTP connection... Please wait.'):
                result = test_smtp(
                    host=smtp_host,
                    port=smtp_port,
                    encryption=encryption_type,
                    user=smtp_user,
                    password=smtp_password,
                    from_addr=sender_email,
                    to_addr=recipient_email,
                    subject=email_subject,
                    body=email_body,
                    timeout=timeout_sec
                )
            # Display the final result
            if "Success" in result:
                st.success(result)
            else:
                st.error(result)
