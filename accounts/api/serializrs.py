from django.core.exceptions import ValidationError
from rest_framework import serializers
from ..models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=300, write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','token']

        extra_kwargs={
            'password': {'write_only': True}
		}
	    
# class LoginSerializer(serializers.Serializer):
# 	email = serializers.EmailField(max_length=255)
# 	password = serializers.CharField(max_length=150)
# 	token = serializers.CharField(max_length=500,allow_null=True,allow_blank=True)

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=70)
    token = serializers.CharField(max_length=300, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'token', 'password')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self,data):
	    username = data.get('username')	
	    password = data.get('password')
	    if not username:
		    raise ValidationError('Enter your username')
                    
	    user = User.objects.filter(username=username)
	    if user.exists():
		    user_obj = user.first() 
	    else:
		    raise ValidationError('Username not found')
        
	    if user_obj:
		    if not user_obj.check_password(password):
			    raise ValidationError('Password is incorrect')
		    data['token'] = 'some random token'
	    return data
	

class UserUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username']
		read_only_fields = [
			'email',
		]       

class UserChangePasswordSerializer(serializers.Serializer):
	oldPassword = serializers.CharField(max_length=150)
	newPassword1 = serializers.CharField(max_length=150)
	newPassword2 = serializers.CharField(max_length=150)

class UserResetPasswordSerializer(serializers.Serializer):
	email = serializers.EmailField(max_length=60)	

class UserResetPasswordVerifySerializer(serializers.Serializer):
	new_password = serializers.CharField(max_length=128)

    
