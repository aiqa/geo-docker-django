from rest_framework import generics

from ...models.river import River
from ...serializers.river_serializers import RiverSerializer


class RiverList(generics.ListCreateAPIView):
    queryset = River.objects.all().order_by('-created_at')
    serializer_class = RiverSerializer
