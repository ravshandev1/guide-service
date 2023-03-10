from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact_link', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']

# Register your models here.
