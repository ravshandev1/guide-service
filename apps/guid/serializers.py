from rest_framework import serializers
from .models import Language, City, Rate, WorkOfGuid, Guid, Booking


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'get_image', 'description']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['rate', 'guid']


class WorkOfGuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOfGuid
        fields = ['get_image', 'video']


class GuidDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guid
        fields = ['id', 'name', 'get_image', 'bio', 'get_rating', 'language', 'works']

    works = WorkOfGuidSerializer(many=True, read_only=True)


class GuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guid
        fields = ['name', 'get_rating']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['guid', 'name', 'email', 'city', 'check_in_time', 'check_out_time', 'contact_link', 'created_at']
    created_at = serializers.DateTimeField(read_only=True)
