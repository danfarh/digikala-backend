from django.urls import path
from accounts.api import views
from dj_rest_auth.views import (UserDetailsView,
                                LoginView,
                                LogoutView,
                                PasswordChangeView,
                                PasswordResetView,
                                PasswordResetConfirmView)
from dj_rest_auth.registration.views import RegisterView
app_name='accounts'
urlpatterns = [
    # custom auth
    path('custom/register/', views.RegisterUser.as_view() , name='custom-register'),
    path('custom/login/', views.LoginUser.as_view() , name='custom-login'),
    path('custom/login2/', views.LoginUserView.as_view() , name='custom-login2'),
    path('custom/password/change/', views.UserChangePassword.as_view() , name='custom_password_change'),
    path('revoke/token/', views.RevokeToken.as_view() , name='revoke'),
    path('user/update/', views.UpdateUser.as_view() , name='update'),
    path('custom/password/reset/', views.UserResetPassword.as_view() , name='reset'),
    path('custom/password/reset/verify/', views.UserResetPasswordVerify.as_view() , name='reset-verify'),
    path('get/verification/code/', views.get_verification_code , name='get_verification_code'),
    path('check/verification/code/', views.check_verification_code , name='check_verification_code'),


    # dj-rest-auth override
    path('user/', UserDetailsView.as_view(), name='user_details'),
    path('login/', LoginView.as_view() , name='login'),
    path('register/', RegisterView.as_view() , name='register'),
    path('password/change/', PasswordChangeView.as_view() , name='password-change'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('logout/', LogoutView.as_view() , name='logout'),
   
   
]

