from django.db import models
from django.utils import timezone


class country_data(models.Model):
    country= models.CharField(max_length=200)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.country} - {self.date_time}'
        
