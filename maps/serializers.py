from rest_framework import serializers
from maps.models import Location

# Location serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
