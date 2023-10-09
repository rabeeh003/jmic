from django.contrib import admin
from .models import user_accounts,admin_accounts, batchs
# Register your models here.

admin.site.register(batchs)
admin.site.register(admin_accounts)
admin.site.register(user_accounts)