from django.urls import path
from .views import batchome,batchedit,deleteobj,addstu

# app_name = 'teacher'

urlpatterns = [
    path('batchome/',batchome, name='batchome'),
    path("addstu/", addstu, name="addstu"),
    path('<int:pk>/',batchedit, name='edit'),
    path('del/<int:pk>/',deleteobj, name='del'),
    # path('',std.as_view(), name='std')
]
