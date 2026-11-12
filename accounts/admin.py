from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('UEH details', {'fields': ('role', 'business_name', 'phone')}),
    )
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role',)