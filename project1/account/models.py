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
    


# New models .
class Teacher(models.Model):
    teacherid = models.CharField( max_length=10)
    t_name = models.CharField(max_length=200,)
    t_dob = models.DateField(auto_now=False, auto_now_add=False)
    t_mail = models.EmailField(max_length=254, unique=True)
    t_phone = models.BigIntegerField(max_length=10, unique=True)

    def _str_(self):
        return self.t_name

class Batch(models.Model):
    batch_no = models.CharField(max_length=3, unique=True)
    batch_year = models.IntegerField(max_length=4)
    batch_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.batch_no

class Sem(models.Model):
    sem = models.IntegerField(max_length=10)
    count_of_sub = models.IntegerField(max_length=2,default=0)
    sub1 = models.CharField( max_length=50, default='no subject')
    sub2 = models.CharField( max_length=50, default='no subject')
    sub3 = models.CharField( max_length=50, default='no subject')
    sub4 = models.CharField( max_length=50, default='no subject')
    sub5 = models.CharField( max_length=50, default='no subject')
    sub6 = models.CharField( max_length=50, default='no subject')
    sub7 = models.CharField( max_length=50, default='no subject')
    sub8 = models.CharField( max_length=50, default='no subject')
    sub9 = models.CharField( max_length=50, default='no subject')
    sub10 = models.CharField( max_length=50, default='no subject')
    sub11 = models.CharField( max_length=50, default='no subject')
    sub12 = models.CharField( max_length=50, default='no subject')
    sub13 = models.CharField( max_length=50, default='no subject')
    sub14 = models.CharField( max_length=50, default='no subject')
    sub15 = models.CharField( max_length=50, default='no subject')

    def __str__(self):
        return f"{self.sem}"

class Student(models.Model):
    studentid = models.CharField(max_length=12, unique=True)
    st_name = models.CharField(max_length=200)
    st_dob = models.DateField(auto_now=False, auto_now_add=False)
    st_batch = models.ForeignKey(Batch, on_delete=models.CASCADE )
    st_mail = models.EmailField(max_length=254, unique=True)
    st_phone = models.BigIntegerField(max_length=10)

    def _str_(self):
        return f"{self.st_nam}"
    
class Mark(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem_no = models.ForeignKey(Sem, on_delete=models.DO_NOTHING)
    count_subject = models.IntegerField(max_length=2, default=0)
    s1 = models.IntegerField(max_length=3, default=0)
    s2 = models.IntegerField(max_length=3, default=0)
    s2 = models.IntegerField(max_length=3, default=0)
    s3 = models.IntegerField(max_length=3, default=0)
    s4 = models.IntegerField(max_length=3, default=0)
    s5 = models.IntegerField(max_length=3, default=0)
    s6 = models.IntegerField(max_length=3, default=0)
    s7 = models.IntegerField(max_length=3, default=0)
    s8 = models.IntegerField(max_length=3, default=0)
    s9 = models.IntegerField(max_length=3, default=0)
    s10 = models.IntegerField(max_length=3, default=0)
    s11 = models.IntegerField(max_length=3, default=0)
    s12 = models.IntegerField(max_length=3, default=0)
    s13 = models.IntegerField(max_length=3, default=0)
    s14 = models.IntegerField(max_length=3, default=0)
    s15 = models.IntegerField(max_length=3, default=0)