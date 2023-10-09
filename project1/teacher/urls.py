from django.urls import path
from .views import batchome

urlpatterns = [
    path('batchome/',batchome,name='batchome'),
]
