from django.urls import path
from .views import main

urlpatterns = [
    path('music_control', main)
]
