from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, authentication, permissions
from .serializers import SubscribeSerializer, SubscriptionSerializer
from .models import Subscriber, Subscription, Plan
# Create your views here.



class SubcriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    
    def perform_create(self, serializer):
        """
        Called after serializer.is_valid() and before saving to DB.
        Override this to customize how objects are saved.
        """
        self.subscription = serializer.save()
    
    def create(self, request, *args, **kwargs):
        """
        Override this to customize the full save-response flow.
        """
        response = super().create(request, *args, **kwargs)
        # Replace response.data if needed:
        response.data = SubscriptionSerializer(self.subscription).data
        return response
    

class SubscriptionDeleteView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def delete(self, request, *args, **kwargs):
        print(f'deleted object={self.get_object()}')
        return super().delete(request, *args, **kwargs)