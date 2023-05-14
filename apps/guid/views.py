from rest_framework import generics, response
import requests
from .models import Guid, Language, City, Booking, Rate
from .serializers import CityListSerializer, LanguageSerializer, GuidSerializer, GuidDetailSerializer, \
    BookingSerializer, CityDetailSerializer, RateSerializer
from django.conf import settings
from datetime import datetime, timedelta
import pytz


class RateAPI(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class CityAPI(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer


class CityDetailAPI(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class GuidAPI(generics.ListAPIView):
    queryset = Guid.objects.all()
    serializer_class = GuidSerializer


class LanguageAPI(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class GuidRetrieveAPI(generics.RetrieveAPIView):
    queryset = Guid.objects.all()
    serializer_class = GuidDetailSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        obj = Guid.objects.filter(id=self.kwargs['pk']).first()
        date = datetime.now(pytz.timezone(settings.TIME_ZONE))
        bookings = Booking.objects.filter(guid=obj, check_in_time__gt=date, is_checked=True).all()
        lst = list()
        min_month = [i.check_in_time for i in bookings]
        max_month = [i.check_out_time for i in bookings]
        if min_month and max_month:
            mn_in = min(min_month)
            mn_ou = max(max_month)
            j = mn_in
            while j <= mn_ou:
                lst.append(j.__format__('%Y-%m-%d'))
                j = j + timedelta(days=1)
        data['days'] = lst
        return response.Response(data)


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
        cre = serializer.data['created_at'][:10]
        cre_t = serializer.data['created_at'][11:16]
        text = (f"Booking",
                f"Guid - {serializer.data['guid_name']}",
                f"Name - {serializer.data['name']}",
                f"email - {serializer.data['email']}",
                f"City - {serializer.data['city_name']}",
                f"Language - {serializer.data['language_name']}",
                f"Check in time - {day_in + ' ' + time_in}",
                f"Check out time - {day_out + ' ' + time_out}",
                f"Contact - {serializer.data['contact_link']}",
                f"Created at - {cre + ' ' + cre_t}")
        requests.get(url=f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
                     params={'text': '\n'.join(text), 'chat_id': settings.ADMIN})
        return response.Response({'success': True})
