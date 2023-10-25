from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import threading
from .models import EmailForNotification

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_message_notification_to_company(message):
    email_subject = 'New Message Received! | DeluxeDays'
    email_body = render_to_string('messageNotificationEmail.html', {
        'fullname': message.firstname + ' ' + message.lastname,
        'email': message.email,
        'phone': message.phone_number,
        'message': message.message
    })

    # Get all email addresses from the 'Email' model
    email_objects = EmailForNotification.objects.all()

    # Extract email addresses from the queryset and store them in a list
    email_addresses = [email_obj.email for email_obj in email_objects]
    
    email = EmailMessage(
        subject=email_subject, body=email_body,
        from_email=settings.EMAIL_FROM_USER,
        to=email_addresses
    )
    email.content_subtype = "html"

    EmailThread(email).start()