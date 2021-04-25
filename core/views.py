from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .constants import MAX_BOTS_PER_USER
from .models import TelegramData
from .permissions import IsTheOwnerOf
from .serializers import TelegramDataSerializer


class TelegramDataViewSet(viewsets.ModelViewSet):
    """
    View set for ``TelegramData``
    Function:
        ``list`` 
        ``retrive``
        ``update`` 
        ``partial_update``
        ``create`` 
        ``destoy``
    """
    queryset = TelegramData.objects
    serializer_class = TelegramDataSerializer
    permission_classes = [IsAuthenticated, IsTheOwnerOf]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Check maximum bots per user
        if (TelegramData.objects.filter(owner=self.request.user).count() >= MAX_BOTS_PER_USER):
            raise PermissionDenied(detail = 'maximum amount of bots per user reached')
        serializer.save(owner=self.request.user)