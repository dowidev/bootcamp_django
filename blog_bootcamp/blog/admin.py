from django.contrib import admin

# Register your models here.
from .models import Category, New

admin.site.register(Category)
admin.site.register(New)