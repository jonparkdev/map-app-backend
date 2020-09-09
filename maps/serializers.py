from rest_framework import serializers
from maps.models import Location

# Location serializers

class LocationSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'owner', 'name', 'latitude', 'longitude', 'owner_name')

    def get_owner_name(self, user):
        return f'{user.owner.first_name} {user.owner.last_name}'
