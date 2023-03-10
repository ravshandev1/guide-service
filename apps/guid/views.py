from rest_framework import generics, response
import requests
from .models import Guid, Language, City, Booking
from .serializers import CitySerializer, LanguageSerializer, GuidSerializer, GuidDetailSerializer, BookingSerializer
from django.conf import settings


class CityAPI(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class GuidAPI(generics.ListAPIView):
    queryset = Guid.objects.all()
    serializer_class = GuidSerializer


class LanguageAPI(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class GuidRetrieveAPI(generics.RetrieveAPIView):
    queryset = Guid.objects.all()
    serializer_class = GuidDetailSerializer


class BookingAPI(generics.GenericAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        day_in = serializer.data['check_in_time'][:10]
        time_in = serializer.data['check_in_time'][11:16]
        day_out = serializer.data['check_out_time'][:10]
        time_out = serializer.data['check_out_time'][11:16]
        cre = serializer.data['check_out_time'][:10]
        cre_t = serializer.data['check_out_time'][11:16]
        text = (f"Guid - {serializer.data['guid']}",
                f"Name - {serializer.data['name']}",
                f"email - {serializer.data['email']}",
                f"Check in time - {day_in + ' ' + time_in}",
                f"Check out time - {day_out + ' ' + time_out}",
                f"Contact - {serializer.data['contact_link']}",
                f"Created at - {cre + ' ' + cre_t}")
        requests.get(url=f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
                     params={'text': '\n'.join(text), 'chat_id': settings.ADMIN})
        return response.Response({'success': True})
