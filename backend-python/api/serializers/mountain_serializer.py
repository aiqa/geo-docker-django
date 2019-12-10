from rest_framework import serializers
from ..models.mountain import Mountain


class MountainSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(source='created_at', required=False)

    class Meta:
        model = Mountain
        fields = ('id', 'name', 'height', 'createdAt',)
