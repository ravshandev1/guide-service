from django.contrib import admin
from .models import Contact, About, Place
from guid.translation import CustomTranslationsAdmin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact_link', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']


@admin.register(About)
class Admin(CustomTranslationsAdmin):
    list_display = ['id', 'address']


@admin.register(Place)
class Admin(admin.ModelAdmin):
    list_display = ['id']
