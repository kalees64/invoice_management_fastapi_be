import smtplib
from email.message import EmailMessage

def send_email(email: str, subject: str, body: str, html: str = "", pdf: bytes | None = None ):
    try:

        EMAIL = "vkalees64@gmail.com"
        PASSWORD = "tgakypumzwasqrou"

        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = email
        msg["Subject"] = subject
        if html == "":
            msg.set_content(body)
        else:
            msg.add_alternative(html, subtype="html")
        if pdf:
            msg.add_attachment(pdf, "application/pdf", "utf-8")
        

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise e