from django.urls import path
from .views import batchome

# app_name = 'teacher'

urlpatterns = [
    path('batchome/',batchome, name='batchome'),
    # path('',std.as_view(), name='std')
]
