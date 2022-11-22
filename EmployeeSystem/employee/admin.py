from django.contrib import admin
from .models import Employee

# Registering Employee model so that it can be visible in admin site.
admin.site.register(Employee)