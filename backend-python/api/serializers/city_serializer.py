from rest_framework import serializers
from ..models import City


class CitySerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(source='created_at', required=False)

    class Meta:
        model = City
        fields = ('id', 'name', 'population', 'createdAt',)
