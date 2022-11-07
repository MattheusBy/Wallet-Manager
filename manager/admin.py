from django.contrib import admin

from manager.models import UserProfile, Category, Transaction
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(UserProfile),
admin.site.register(Category),
admin.site.register(Transaction)
