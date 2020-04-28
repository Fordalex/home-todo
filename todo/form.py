from django import forms
from django.forms import ModelForm
from .models import Task, Food, Messages

class inputTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'complete', 'notes')

class inputFood(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('name', 'complete', 'notes')

class inputMessages(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ('name', 'message', 'colour')