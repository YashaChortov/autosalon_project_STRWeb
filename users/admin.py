from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_client', 'is_employee', 'is_superuser', 'is_active')
    list_filter = ('is_client', 'is_employee', 'is_superuser', 'is_staff', 'is_active')

    add_form = UserCreationForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_client', 'is_employee'),
        }),
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Роли сайта', {'fields': ('is_client', 'is_employee')}),
    )