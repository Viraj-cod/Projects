from django.urls import path
from . import views
urlpatterns = [
    path('Index/',views.Index,name='home'),
    path('',views.show,name='show'),
    path('edit/ <int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('search/',views.search,name='search')
]
