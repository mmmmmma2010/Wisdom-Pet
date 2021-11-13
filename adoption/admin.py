from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Pet
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display=["name","age","sex"]
