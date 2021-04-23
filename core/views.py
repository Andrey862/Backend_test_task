from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

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
        serializer.save(owner=self.request.user)