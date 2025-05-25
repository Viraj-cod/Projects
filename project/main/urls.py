from django.urls import path
from . import views

urlpatterns = [
    path('',views.check,name='main'),
    path('gal/',views.gal,name="gallery"),
    path('abt/',views.abt,name="about"),
    path('price/',views.price,name="pricing"),
    path('cnt/',views.cnt,name="contact"),

]
