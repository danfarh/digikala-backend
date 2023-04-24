import math,random
from django.conf import settings
from kavenegar import *

# generate verification code
def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random()*10)]
    return OTP 

# send sms def
def send_sms(phoneNumber,message):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params = {
            'sender' : '10004346',
            'receptor': phoneNumber,
            'message' : message
        }
        response = api.sms_send(params) 
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)    
#send_sms('09389505414',f"your verification code is {generate_otp()}.")    
