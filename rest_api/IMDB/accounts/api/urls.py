from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token #inbuilt

from accounts.api.views import register,logout
urlpatterns = [
    path('login',obtain_auth_token,name='login'),
    path('register/',register,name='register'),
    path('logout',logout.as_view(),name='register')
]
