from rest_framework import generics

from ..serializers.mountain_serializer import MountainSerializer
from ..models import Mountain


class MountainList(generics.ListCreateAPIView):
    queryset = Mountain.objects.all().order_by('-created_at')
    serializer_class = MountainSerializer


class MountainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
