from django.contrib import admin
from . models import transactions_model,Trainers_model,accesories_model,members_model

admin.site.register(members_model)
admin.site.register(transactions_model)
admin.site.register(Trainers_model)
admin.site.register(accesories_model)