from django.contrib import admin
from .models import CustomUser, Contact


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'photo')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'created')
