from django.db import models
from django.utils import timezone
from .manager import UserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
                            AbstractBaseUser,   
                            BaseUserManager,
                            AbstractUser,
                            _user_get_permissions,
                            PermissionsMixin,
                            Group,
                            Permission
                            )
from django.core.validators import MinLengthValidator
import datetime


# class User(AbstractUser):
#     pass

def phone_validate(value):
    if len(value) != 11:
        raise ValidationError(
            _('%(value)s Phone number must be an 11 character'),
            params={'value': value},
        )
    if not value.isnumeric():
         raise ValidationError(
            _('%(value)s Phone number must be a number'),
            params={'value': value},
        )

class User(AbstractBaseUser, PermissionsMixin):
    first_name              = models.CharField(max_length=100)
    last_name               = models.CharField(max_length=100)
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    password                = models.CharField(max_length=100,validators=[MinLengthValidator(8)])
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active				= models.BooleanField(default=True)
    is_admin				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    phone_number            = models.CharField(max_length=15, blank=True, validators=[phone_validate])
    address                 = models.TextField(blank=True) 
    user_permissions        = models.ManyToManyField(
                                Permission,
                                verbose_name=_('user permissions'),
                                blank=True,
                                help_text=_('Specific permissions for this user.'),
                                related_name="user_sets",
                                related_query_name="user",
                            )
    groups                  = models.ManyToManyField(
                                Group,
                                blank=True,
                            )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
    objects = UserManager()
        
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def get_user_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'user')
    
    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'all')

    def __str__(self):
	    return f"{self.username}"    
    

def user_profile_image_path(instance, filename):
    now = datetime.datetime.now()
    return 'accounts/profile_image/{0}/{1}/{2}/user_{3}/{4}'.format(
        now.strftime("%Y"),
        now.strftime("%m"),
        now.strftime("%d"),
        instance.user.id,
        filename)

class Profile(models.Model):
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=user_profile_image_path,blank=True,null=True,)
    age = models.PositiveIntegerField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.__str__()
