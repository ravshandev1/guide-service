from django.urls import path
from .views import GuidAPI, CityAPI, LanguageAPI, GuidRetrieveAPI, BookingAPI

urlpatterns = [
    path('city/', CityAPI.as_view()),
    path('language/', LanguageAPI.as_view()),
    path('', GuidAPI.as_view()),
    path('<int:pk>/', GuidRetrieveAPI.as_view()),
    path('booking/', BookingAPI.as_view()),
]
