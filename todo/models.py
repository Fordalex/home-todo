from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):

    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True, default="")
    category = models.CharField(max_length=200, default="")
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    complete = models.BooleanField(blank=True)

    def __str__(self):
        return self.name