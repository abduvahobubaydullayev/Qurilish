from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Firm, CustomUser
from .form import *

# Register your models here.

admin.site.register(Firm)


class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'image', 'auth', 'firm', 'phone_number', 'email')

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('image', 'auth', 'firm', 'phone_number', 'email')}),
    # )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('image', 'auth', 'firm', 'phone_number', 'email')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
