"""todoManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from todo.views import index, addTask, deleteTask, editTask, toggleTask, toggleFood, message, addFood, deleteFood, deleteMessage

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^addTask', addTask, name="addTask"),
    url(r'^edit/(?P<id>\d+)$', editTask),
    url(r'^delete/(?P<id>\d+)$', deleteTask),
    url(r'^deleteFood/(?P<id>\d+)$', deleteFood),
    url(r'^deleteMessage/(?P<id>\d+)$', deleteMessage),
    url(r'^message/$', message, name="message"),
    url(r'^toggle/(?P<id>\d+)$', toggleTask),
    url(r'^toggleFood/(?P<id>\d+)$', toggleFood),
    url(r'^addFood/$', addFood, name="addFood"),
]
