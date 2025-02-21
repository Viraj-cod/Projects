from django.contrib import admin
from . models import Watchlist,Review,platform
# Register your models here.

admin.site.register(Watchlist)
admin.site.register(Review)
admin.site.register(platform)