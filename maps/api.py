from maps.models import Location
from rest_framework import viewsets, permissions
from maps.serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LocationSerializer

    def get_queryset(self):
        return self.request.user.locations.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # possibly add trigger to update cache
