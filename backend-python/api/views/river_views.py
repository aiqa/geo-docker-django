from rest_framework import generics

from ..models import River
from ..serializers.river_serializers import RiverSerializer


class RiverList(generics.ListCreateAPIView):
    queryset = River.objects.all().order_by('-created_at')
    serializer_class = RiverSerializer


class RiverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = River.objects.all()
    serializer_class = RiverSerializer
