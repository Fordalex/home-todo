from django.contrib import admin
from .models import Task, Food, Messages, Dinner

# Register your models here.
admin.site.register(Task)
admin.site.register(Food)
admin.site.register(Messages)
admin.site.register(Dinner)