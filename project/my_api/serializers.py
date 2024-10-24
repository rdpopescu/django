from rest_framework import serializers

from locations.models import Location


class LocationSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'country']