"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path,include
from rest_framework.authtoken.views import obtain_auth_token
#swagger
from .yasg import schema_view
from search.views import SearchProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    #search
    path('search/' , SearchProductView.as_view({'get': 'list'})),
    #google auth
    path('accounts/', include('allauth.urls')), #http://127.0.0.1:8000/accounts/google/login/
                                                #http://127.0.0.1:8000/accounts/google/login/callback/
    path('api-auth/', include('rest_framework.urls')),
    path('api/token-auth/', obtain_auth_token),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('accounts.urls')),
    path('product/', include('product.urls')),
    path('comment/', include('comment.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('category/', include('category.urls')),
    path('discount/', include('discount.urls')),

    #swagger urls
   	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG == True:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


AdminSite.site_header = 'Administration'
AdminSite.index_title = 'Digikala'
AdminSite.site_title = 'Digikala Admin'    