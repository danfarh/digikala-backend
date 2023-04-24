from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import jwt
from accounts.models import User
async def get_user(request):
    return Response({'user': str(request.user)})

async def is_auth(handler):
    async def middleware(request):
        JWT_SECRET = 'secret'
        JWT_ALGORITHM = 'HS256'
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return Response({'message': 'Token is invalid'}, status=400)

            request.user = get_object_or_404(User,email=payload['email'])  
        return await handler(request)
    return middleware
