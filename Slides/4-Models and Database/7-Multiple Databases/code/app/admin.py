from django.contrib import admin
from . models import User
from . site.new_admin import MultiDBModelAdmin,MultiDBTabularInline 

# Register your models here.

class UserInline(MultiDBTabularInline):
    model = User


# registering the site in the new admin site
othersite=admin.AdminSite('othersite')
othersite.register(User,MultiDBModelAdmin)
