from django.contrib import admin
from .models import Bank_Account,Movement,Transfer

admin.site.register(Movement)
admin.site.register(Bank_Account)
admin.site.register(Transfer)