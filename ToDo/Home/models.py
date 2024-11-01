from django.db import models

# Create your models here.

class Information(models.Model):
    task = models.TextField(default=None)
    date = models.TextField(default=None)

    def __str__(self):
        return self.task

