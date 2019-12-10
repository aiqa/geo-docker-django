from rest_framework import generics

from ...serializers.mountain_serializer import MountainSerializer
from ...models.mountain import Mountain


class MountainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
