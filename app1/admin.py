from django.contrib import admin
from .models import Bank_Account,Movement

admin.site.register(Movement)
admin.site.register(Bank_Account)