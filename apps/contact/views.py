from rest_framework import generics, response
from .serializers import ContactSerializer, AboutSerializer, PlaceSerializer
from .models import Contact, About, Place
import requests
from django.conf import settings


class PlacesAPI(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class AboutAPI(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactAPI(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        day_in = serializer.data['check_in_time'][:10]
        time_in = serializer.data['check_in_time'][11:16]
        day_out = serializer.data['check_out_time'][:10]
        time_out = serializer.data['check_out_time'][11:16]
        cre = serializer.data['created_at'][:10]
        cre_t = serializer.data['created_at'][11:16]
        text = (f"Contact",
                f"City - {serializer.data['city_name']}",
                f"Name - {serializer.data['name']}",
                f"email - {serializer.data['email']}",
                f"language - {serializer.data['language_name']}",
                f"Check in time - {day_in + ' ' + time_in}",
                f"Check out time - {day_out + ' ' + time_out}",
                f"Contact - {serializer.data['contact_link']}",
                f"Created at - {cre + ' ' + cre_t}")
        requests.get(url=f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
                     params={'text': '\n'.join(text), 'chat_id': settings.ADMIN})
        return response.Response({'success': True})
