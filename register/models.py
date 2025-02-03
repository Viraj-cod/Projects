
from django.db import models

class empty(models.Model):
    user_ptr = models.CharField(max_length=20,null=True, default='hello')  # Default to User ID 1
