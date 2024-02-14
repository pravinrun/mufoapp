# # from django.conf import settings
# from twilio.rest import Client 
# from Mufo import settings

# def send_otp_on_phone(phone_number, otp):
#     account_sid = settings.account_sid
#     auth_token = settings.auth_token
#     twilio_phone_number = settings.twilio_phone_number
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#         body=f"Your OTP is: {otp}",
#         from_=twilio_phone_number,
#         to=phone_number
#     )

#     return message.sid

# import requests

# def send_otp_on_phone(mobile_number, otp):
#     API_KEY = '397239AMFkn6shwxk64787c77P1'
#     SENDER_ID = '998765'
#     ROUTE = '4'
#     Templte_id =  "64787cd3d6fc050aa44d0932"

#     url = "https://control.msg91.com/api/v5/otp"
#     headers = {
#         "Content-Type": "application/json",
#         "authkey": API_KEY
#     }
#     payload = {
#         "template_id": Templte_id ,  
#         "mobile": mobile_number,
#         "OTP": otp,
#         "sender": SENDER_ID,
#         "route": ROUTE
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     print(response)
#     if response.status_code == 200:
#         # OTP sent successfully
#         return True
#     else:
#         # Failed to send OTP
#         return False
    
# import requests

# def send_otp_on_phone(mobile_number, otp):
#     API_KEY = '397239AMFkn6shwxk64787c77P1'
#     SENDER_ID = '998765'
#     ROUTE = '4'
#     Template_id =  "64787cd3d6fc050aa44d0932"

#     url = "https://control.msg91.com/api/v5/otp"
#     headers = {
#         "Content-Type": "application/json",
#         "authkey": API_KEY
#     }
#     payload = {
#         "template_id": Template_id ,  
#         "mobile": mobile_number,
#         "OTP": otp,
#         "sender": SENDER_ID,
#         "route": ROUTE
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     if response.status_code == 200:
#         # OTP sent successfully
#         return True
#     else:
#         # Failed to send OTP
#         return False


import requests

def send_otp_on_phone(mobile_number, otp):
    # Replace these values with your actual API key, sender ID, and template ID
    API_KEY = 'your_api_key_here'
    SENDER_ID = 'your_sender_id_here'
    TEMPLATE_ID = 'your_template_id_here'

    url = "https://api.example.com/send_otp"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "mobile_number": mobile_number,
        "otp": otp,
        "sender_id": SENDER_ID,
        "template_id": TEMPLATE_ID
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # OTP sent successfully
        return True
    else:
        # Failed to send OTP
        return False
