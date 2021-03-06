from rest_framework import generics

from ...models.city import City
from ...serializers.city_serializer import CitySerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all().order_by('-created_at')
    serializer_class = CitySerializer
