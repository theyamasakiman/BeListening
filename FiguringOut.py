# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

email_key = "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"
message = Mail(
    from_email='cky8@uw.edu',
    to_emails='cky8@uw.edu',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(email_key)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
