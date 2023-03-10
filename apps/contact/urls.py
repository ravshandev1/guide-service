from django.urls import path
from .views import ContactAPi

urlpatterns = [
    path('', ContactAPi.as_view()),
]
