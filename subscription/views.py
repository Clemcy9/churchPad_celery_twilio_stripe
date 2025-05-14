from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .serializers import SubscriberSerializer
# Create your views here.


class SubcriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriberSerializer
    
    # def get_queryset(self):
    #     return super().get_queryset()