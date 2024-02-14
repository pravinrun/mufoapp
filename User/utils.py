# utils.py
import string
import random
from twilio.rest import Client
from django.core.mail import send_mail  # Corrected import statement

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

def send_otp_phone(phone_number, otp):
    account_sid = 'your_account_sid'  # Replace with your Twilio account SID
    auth_token = 'your_auth_token'  # Replace with your Twilio auth token
    twilio_phone_number = 'your_twilio_phone_number'  # Replace with your Twilio phone number

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your OTP is: {otp}',
        from_=twilio_phone_number,
        to=phone_number
    )
