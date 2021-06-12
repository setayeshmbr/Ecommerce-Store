from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from account.models import User
UserAdmin.fieldsets[2][1]['fields'] = (
    'is_staff',
    'is_superuser',
    'groups',
    'user_permissions'
)
UserAdmin.list_display +=('is_superuser',)

admin.site.register(User, UserAdmin)