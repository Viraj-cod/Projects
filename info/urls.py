from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.members,name='mem'),
    path('accesories/',views.accesories,name='ace'),
    path('trainers/',views.Trainers,name='train'),
    path('transactions/',views.Transactions,name='transe'),
    path('add_members/',views.add_members,name='add_mem'),
    path('add_accesories/',views.add_accesories,name='add_ace'),
    path('add_trainers/',views.add_trainers,name='add_train'),
    path('add_transactions/',views.add_Transactions,name='add_transe'),
    path('mem/<int:id>/',views.mem_delete,name='mem_delete'),
    path('ace/<int:id>/',views.accesories_delete,name='ace_delete'),
    path('train/<int:id>/',views.trainer_delete,name='train_delete'),
    path('transe/<int:id>/',views.transaction_delete,name='transe_delete'),
    path('search_mem/',views.search_mem,name='search_mem'),
    path('search_ace/',views.search_ace,name='search_ace'),
    path('search_train/',views.search_train,name='search_train'),
    path('search_transe/',views.search_transe,name='search_transe'),
    path('mem_report/',views.mem_rep,name='mem_repo'),
    path('ace_report/',views.ace_rep,name='ace_repo'),
    path('train_report/',views.train_rep,name='train_repo'),
    path('transe_report/',views.transe_rep,name='transe_repo'),
    path('gallery/',views.gallery,name = 'gal'),
    #path('about/',views.about,name= 'about'),
    path('pricing/',views.price,name='price'),
    path('under/<str:name>/',views.under,name='under')
    
]
