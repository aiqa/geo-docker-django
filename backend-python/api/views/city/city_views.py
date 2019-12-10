from rest_framework import generics

from ...models.city import City
from ...serializers.city_serializer import CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
