import smtplib
import imghdr
from email.message import EmailMessage
from email.policy import default

# Enter emailing details bellow:
PASSWORD = ""
SENDER = ""
RECEIVER = ""


def send_email(image_path):
    print("send_email function start.")
    email_message = EmailMessage(policy=default)
    email_message["Subject"] = "Object Detected"
    email_message.set_content('A new object has entered the field.')

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function end.")


if __name__ == "__main__":
    send_email("images/19.png")
    print("Email Sent.")


