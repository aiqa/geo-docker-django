from rest_framework import serializers

from ..models import River


class RiverSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(source='created_at', required=False)

    class Meta:
        model = River
        fields = ('id', 'name', 'length', 'createdAt',)
