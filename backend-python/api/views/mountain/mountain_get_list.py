from rest_framework import generics

from ...serializers.mountain_serializer import MountainSerializer
from ...models.mountain import Mountain


class MountainList(generics.ListCreateAPIView):
    queryset = Mountain.objects.all().order_by('-created_at')
    serializer_class = MountainSerializer
