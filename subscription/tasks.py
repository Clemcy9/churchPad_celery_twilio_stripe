from celery import shared_task
from twilio.rest import Client
import os
@shared_task
def send_welcome_sms(name, phone_number):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    message_body = f"Hi {name}, thanks for subscribing to our livestream service on ChurchPad!"

    client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=phone_number
    )

    return f'message sent to {name} with no. {phone_number}'
