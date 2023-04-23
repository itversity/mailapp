import os
import sys
import ssl
import logging
from sendgrid.helpers.mail import Mail


def send_greeting(sg_client, from_email, to_emails, subject, message):
    ssl._create_default_https_context = ssl._create_unverified_context
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=message
    )
    try:
        response = sg_client.send(message)
        logging.info(response.status_code)
        return response
    except Exception as e:
        logging.error(e.message)
        raise


if __name__ == '__main__':
    args = sys.argv
    from_email = args[1]
    to_emails = args[2]
    subject = args[3]
    message = args[4]
    send_greeting(from_email, to_emails, subject, message)