from rest_framework import viewsets

from locations.models import Location
from my_api.serializers import LocationSerializers


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers
