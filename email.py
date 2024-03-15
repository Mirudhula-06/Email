import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_personalized_email(sender_email, sender_password, subject, body, recipients):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = subject

    # Iterate through recipients and personalize the email content
    for recipient in recipients:
        # Customize the email body for each recipient
        personalized_body = f"Dear {recipient['name']},\n\n{body.format(**recipient)}"

        # Attach the personalized body to the email
        message.attach(MIMEText(personalized_body, 'plain'))

        # Set up the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient['email'], message.as_string())
            server.quit()

# Example usage
sender_email = 'your_email@example.com'
sender_password = 'your_email_password'
subject = 'Personalized Greetings'
body = 'Hello {name},\n\nWe appreciate your interest in {interest}.'
recipients = [
    {'name': 'John', 'email': 'john@example.com', 'interest': 'Python programming'},
    {'name': 'Jane', 'email': 'jane@example.com', 'interest': 'Machine learning'},
    # Add more recipients as needed
]

send_personalized_email(sender_email, sender_password, subject, body, recipients)
