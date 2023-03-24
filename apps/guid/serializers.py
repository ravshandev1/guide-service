from rest_framework import serializers
from .models import Language, City, Rate, WorkOfGuid, Guid, Booking


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['contraction', 'name', 'get_image']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'get_image']


class GuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guid
        fields = ['name', 'get_rating']


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'get_image', 'description', 'guids']

    guids = GuidSerializer(many=True, read_only=True)


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['rate', 'guid']


class WorkOfGuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOfGuid
        fields = ['get_image', 'get_video']


class GuidDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guid
        fields = ['id', 'name', 'get_image', 'bio', 'get_rating', 'language', 'works']

    works = WorkOfGuidSerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['guid', 'city_name', 'guid_name', 'name', 'email', 'city', 'check_in_time', 'check_out_time',
                  'contact_link', 'created_at']

    created_at = serializers.DateTimeField(read_only=True)
    city_name = serializers.CharField(read_only=True, source='city.name')
    guid_name = serializers.CharField(read_only=True, source='guid.name')
