import re

from django.db.models import fields
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

    def validate_token(self, token):
        if (not re.match(r"[0-9]{9}:[a-zA-Z0-9_-]{35}", token)):
            raise serializers.ValidationError("Token is invalid")
        return token

    class Meta:
        model = TelegramData
        fields = ['id', 'token', 'title', 'active']
