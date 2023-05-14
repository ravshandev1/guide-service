from django.contrib import admin
from .models import City, Language, Guid, WorkOfGuid, Booking, CityImage, Rate
from .translation import CustomTranslationsAdmin, InlineTranslationsAdmin


@admin.register(Booking)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'guid', 'email', 'city', 'is_read', 'created_at']
    list_filter = ['is_read', 'city', 'created_at']
    search_fields = ['name', 'guid']


class ImageInline(admin.TabularInline):
    model = CityImage
    extra = 0


@admin.register(City)
class CityAdmin(CustomTranslationsAdmin):
    list_display = ['name']
    inlines = [ImageInline]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'contraction']


class WorkOfGuidInline(admin.TabularInline):
    model = WorkOfGuid
    extra = 0


class RateInline(InlineTranslationsAdmin):
    model = Rate
    extra = 0


@admin.register(Guid)
class GuidAdmin(CustomTranslationsAdmin):
    list_display = ['id', 'name', 'rating']
    list_display_links = ('name',)
    inlines = [WorkOfGuidInline, RateInline]
    list_filter = ['language']
    filter_horizontal = ['language', 'city']
