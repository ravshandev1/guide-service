from modeltranslation.translator import register, TranslationOptions
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import City, Guid, Rate
from contact.models import About


class CustomTranslationsAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class InlineTranslationsAdmin(TranslationTabularInline):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(City)
class CityTranslation(TranslationOptions):
    fields = ['name', 'description']


@register(Rate)
class CityTranslation(TranslationOptions):
    fields = ['comment']


@register(About)
class CityTranslation(TranslationOptions):
    fields = ['location', 'address']


@register(Guid)
class LanguageTranslation(TranslationOptions):
    fields = ['name', 'bio']
