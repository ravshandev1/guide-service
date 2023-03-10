from django.urls import path, include
app_name = 'apps'
urlpatterns = [
    path('contact/', include('contact.urls')),
    path('guid/', include('guid.urls')),
]
