from django.contrib import admin

# Register your models here.

from .models import Employee, Points

admin.site.register(Employee)
admin.site.register(Points)