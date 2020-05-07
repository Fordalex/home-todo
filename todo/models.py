from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True, default="")
    category = models.CharField(max_length=200, default="home")
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    complete = models.BooleanField(blank=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True, default="")
    category = models.CharField(max_length=200, default="other")
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    complete = models.BooleanField(blank=True)

    def __str__(self):
        return self.name

class Messages(models.Model):
    name = models.CharField(max_length=150, default="")
    message = models.CharField(max_length=150, default="")
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    colour = models.CharField(max_length=150, default="#fcba03", blank=True)

    def __str__(self):
        return self.name

class Dinner(models.Model):
    name = models.CharField(max_length=150, default="")
    recipe = models.CharField(max_length=150, default="")
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    picture = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.name