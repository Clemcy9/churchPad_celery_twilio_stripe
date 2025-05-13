from rest_framework import serializers
from .models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    plan_id = serializers.CharField()


    class Meta:
        model = Subscriber
        fields = ['phone_number', 'is_active']