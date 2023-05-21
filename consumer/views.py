from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings

from .serializers import (
    ConsumerSerializer,
)


class CreateConsumerView(generics.CreateAPIView):
    """Create a new consumer in the system"""
    serializer_class = ConsumerSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = ConsumerSerializer
    authentication_classes = []
    permission_classes = []

    def get_object(self):
        """Retrieve and return authentication consumer"""
        return self.request.consumer
