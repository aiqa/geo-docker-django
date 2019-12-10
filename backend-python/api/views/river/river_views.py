from rest_framework import generics

from ...models.river import River
from ...serializers.river_serializers import RiverSerializer


class RiverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = River.objects.all()
    serializer_class = RiverSerializer
