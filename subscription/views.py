from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .serializers import SubscribeSerializer
# Create your views here.


class SubcriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer

class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscribeSerializer
    
    # def get_queryset(self):
    #     return super().get_queryset()