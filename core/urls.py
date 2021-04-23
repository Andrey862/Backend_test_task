from django.db import router
from django.urls import include, path
from rest_framework import routers

from . import views

telegram_data = routers.SimpleRouter()
telegram_data.register('', views.TelegramDataViewSet)

urlpatterns = [
    path('telegram_data/', include(telegram_data.urls))
]