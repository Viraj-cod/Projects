from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Watchlist(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=40)
    movie = models.ForeignKey(Watchlist,related_name='review',on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class platform(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    content = models.ManyToManyField(Watchlist,related_name='movies')
    url = models.URLField(max_length=50)

    def __str__(self):
        return self.name