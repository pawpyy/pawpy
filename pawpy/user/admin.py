from django.contrib import admin
from user.models import user,pet
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(user)
admin.site.register(pet)
