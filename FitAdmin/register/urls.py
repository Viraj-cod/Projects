from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registration,name='reg'),
    path('',views.loginview,name='log'),
    path('main/',views.main,name = 'main'),
    path('logout/',views.log_out,name='logout')
]
