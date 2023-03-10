from django.contrib import admin
from .models import City, Language, Guid, WorkOfGuid, Booking
from .translation import CustomTranslationsAdmin


@admin.register(Booking)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'guid', 'email', 'city', 'is_read', 'created_at']



@admin.register(City)
class CityAdmin(CustomTranslationsAdmin):
    list_display = ['id', 'name']


@admin.register(Language)
class LanguageAdmin(CustomTranslationsAdmin):
    list_display = ['id', 'name']


class WorkOfGuidInline(admin.TabularInline):
    model = WorkOfGuid
    extra = 0


@admin.register(Guid)
class GuidAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'language', 'get_rating']
    inlines = [WorkOfGuidInline]
    list_filter = ['language']
