from rest_framework import serializers

from .models import TelegramData


class TelegramDataSerializer(serializers.ModelSerializer):
    """
    Model serializer for Transactions

    Fields:
    ``id`` -- pk
    ``token`` -- string
    ``title`` -- string
    ``active`` -- boolean
    """

    class Meta:
        model = TelegramData
        fields = ['id', 'token', 'title', 'active']
