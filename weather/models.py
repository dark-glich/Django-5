from django.db import models
from django.utils import timezone


class weather_data(models.Model):
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.location} - {self.date_time}'
        