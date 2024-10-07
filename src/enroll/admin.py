from django.contrib import admin
from enroll.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=["Name","Roll_No"]
    list_per_page=3

admin.site.register(User,UserAdmin)