from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact_link', 'city', 'check_in_time', 'check_out_time', 'language']
