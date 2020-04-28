from django.contrib import admin
from .models import Task, Food, Messages

# Register your models here.
admin.site.register(Task)
admin.site.register(Food)
admin.site.register(Messages)