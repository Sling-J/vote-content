from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Poll.as_view(), name='home_url')
]
