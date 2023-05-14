from django.urls import path
from .views import ContactAPI, AboutAPI, PlacesAPI

urlpatterns = [
    path('', ContactAPI.as_view()),
    path('about/', AboutAPI.as_view()),
    path('places/', PlacesAPI.as_view()),
]
