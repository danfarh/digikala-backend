import jwt
from datetime import datetime, timedelta
import os
import binascii
from django.conf import settings

def generateToken(user):
    JWT_SECRET = settings.SECRET_KEY
    JWT_ALGORITHM = 'HS256'
    JWT_EXP_DELTA_SECONDS = 20
    payload = {
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token



def generate_code():
	return binascii.hexlify(os.urandom(20)).decode('utf-8')

