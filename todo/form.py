from django import forms
from django.forms import ModelForm
from .models import Task

class inputTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'complete', 'category', 'notes')