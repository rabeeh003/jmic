from django.contrib import admin
from .models import user_accounts,admin_accounts
from .models import Sem,Teacher,Batch,Student,Mark 
# Register your models here.

# admin.site.register(batchs)
admin.site.register(admin_accounts)
admin.site.register(user_accounts)
# new registrations
admin.site.register(Sem)
admin.site.register(Teacher)
admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Mark)