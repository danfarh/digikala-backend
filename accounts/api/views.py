from django.utils.functional import empty
from django.conf import settings
from ..models import User
from django.shortcuts import get_object_or_404, render,HttpResponse
from rest_framework import serializers, status,generics
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAuthenticated,AllowAny
from utills.tokens import generateToken,generate_code
from utills.redis import redis_set
from utills.sms import generate_otp,send_sms
from ..tasks import task_send_email
from django.core.cache import cache
from .serializrs import (
                UserRegisterSerializer,
                UserLoginSerializer,
                UserUpdateSerializer,
                UserChangePasswordSerializer,
                UserResetPasswordSerializer,
                UserResetPasswordVerifySerializer
                )

import jwt

class RegisterUser(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserRegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
			
            try: 
                user_exists = User.objects.get(email=email)
                if user_exists.is_active:
                    content = {'error': 'Duplicate user.','data': serializer.data}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user = user_exists

            except User.DoesNotExist:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username
                    )
                user.set_password(password) 
                user.save()   
                token = generateToken(user=user) 
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)          
        content = {'message': 'create user successfully.','token':token}    
        return Response(content,status=status.HTTP_200_OK)    


class LoginUser(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = get_object_or_404(User,email=email)
            if user.check_password(password):
                if user.is_active:
                    token = generateToken(user=user)
                    user.token = token
                    user.save()
                    login(request, user)
                    content = {'message': 'login successfully.','data': serializer.data,'token':token}    
                    return Response(content,status=status.HTTP_200_OK) 
            return Response({'user not found'},status=status.HTTP_404_NOT_FOUND)         
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  


class LoginUserView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
                content = {'message': 'login successfully.','data': serializer.data}    
                return Response(content,status=status.HTTP_200_OK)        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  


class RevokeToken(generics.GenericAPIView):
    def delete(self,request):
        request.auth.delete()
        return Response(status=204)  


class UpdateUser(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserUpdateSerializer
    def get_queryset(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request):
        serializer = self.serializer_class(data=request.data, instance=request.user, partial=True)
        if serializer.is_valid():
            serializer.save()
            content = {'success': 'update account.','data': serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class UserChangePassword(generics.GenericAPIView):
    serializer_class = UserChangePasswordSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            oldPassword = serializer.data['oldPassword']
            newPassword1 = serializer.data['newPassword1']
            newPassword2 = serializer.data['newPassword2']
            if request.user.check_password(oldPassword):
                if newPassword1 == newPassword2:
                    request.user.set_password(newPassword1)
                    request.user.save()
                    content = {'success': 'password changed successfully'}
                    return Response(content, status=status.HTTP_200_OK)
                content = {'failed': 'password1 and password2 not match'}    
                return Response(content, status=status.HTTP_400_BAD_REQUEST) 
            content = {'failed': 'your old password is not valid'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class UserResetPassword(generics.GenericAPIView):
    serializer_class = UserResetPasswordSerializer
    permission_classes = [AllowAny, ]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            user =  get_object_or_404(User,email=email)
            if user is not None:
                token = generateToken(user)
                print(token)
                email_data = {
                        'email_subject': 'reset password',
                        'email_body': f'click on this {token}',
                        'email_to': user.email
                    }
                task_send_email.delay(email_data)
                redis_set(f'{user.username}-resetpassword',token,14400)
                content = {'success': 'email sent successfully'}
                return Response(content, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class UserResetPasswordVerify(generics.GenericAPIView):
    serializer_class = UserResetPasswordVerifySerializer
    permission_classes = [AllowAny, ]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        token = request.GET.get('token')
        print(token)
        try:
            if serializer.is_valid():
                new_password = serializer.data.get('new_password')
                payload = jwt.decode(token, settings.SECRET_KEY,'HS256')
                username = payload['username']
                user = get_object_or_404(User,username=username)
                if user is not None:
                    user.set_password(new_password)
                    user.save()
                    content = {'success': 'reset password successfully'}
                    return Response(content, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        except jwt.ExpiredSignatureError:
            return Response({'email': 'Reset link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'email': 'Invalid token!'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'email': 'User not found'}, status=status.HTTP_404_NOT_FOUND)    


#auth with mobile
def get_verification_code(request):
    phone_number = request.GET['phone_number']
    verification_code = generate_otp()
    cache.set(f"verification_code/{phone_number}",verification_code,timeout=25)
    print(f"your verification code is {verification_code}.")
    send_sms(phone_number,f"your verification code is {verification_code}.")
    return HttpResponse('verification code has been sent')

def check_verification_code(request):
    phone_number = request.GET['phone_number']
    verification_code = request.GET['verification_code']
    if verification_code == cache.get(f"verification_code/{phone_number}"):
        return HttpResponse('login successfully.') 
    return HttpResponse('verification code is wrong or expired')

