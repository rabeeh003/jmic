from django.db import models

# Create your models here.
class user_accounts(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    user_pass = models.CharField(max_length=50)
    user_mail = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.user_name

class admin_accounts(models.Model):
    admin_name = models.CharField(max_length=50, unique=True)
    admin_pass = models.CharField(max_length=50)
    admin_mail = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.admin_name

class batchs(models.Model):
    batch_no = models.CharField(max_length=10, unique=True)
    batch_year = models.CharField(max_length=10, unique=True)
    batch_teacher = models.CharField( max_length=50)
    
