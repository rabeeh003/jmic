from django.urls import path
from .views import student

urlpatterns = [
    path('student/',student,name='student'),
]
