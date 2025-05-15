from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, authentication, permissions
from .serializers import SubscribeSerializer, SubscriptionSerializer
from .models import Subscriber, Subscription, Plan
from .tasks import send_welcome_sms


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
        customizing how model is been saved
        """
        response = super().create(request, *args, **kwargs)
        response.data = SubscriptionSerializer(self.subscription).data
        send_welcome_sms.delay(
            response.data["subscriber"]["user"]["username"], 
            response.data["subscriber"]["phone_number"]
        )
        print(f'sent welcom sms to {response.data["subscriber"]["user"]["username"]}')
        return response
    

class SubscriptionDeleteView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def delete(self, request, *args, **kwargs):
        print(f'deleted object={self.get_object()}')
        return super().delete(request, *args, **kwargs)