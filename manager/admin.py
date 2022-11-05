from django.contrib import admin
from rest_framework.authtoken.admin import User

from manager.models import UserProfile
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']


# Register your models here.
admin.site.register(UserProfile),
admin.site.register(User),