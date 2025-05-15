from rest_framework import serializers
from django.utils.translation import gettext as _
from django.db import transaction
from .models import Subscriber, Plan, Subscription
from account.serializers import UserSerializers
from django.contrib.auth import get_user_model

User = get_user_model()

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    
    class Meta:
        model = Subscriber
        fields = ['phone_number', 'user']


class SubscriptionSerializer(serializers.ModelSerializer):
    subscriber = SubscriberSerializer()
    plan = PlanSerializer()
    
    class Meta:
        model = Subscription
        fields = ['plan', 'subscriber', 'is_active']

class SubscribeSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    plan_id = serializers.IntegerField()

    # def validate(self, attrs):
    #     not using this because i want to get or create a user, which will fail if already existing with this method
    #     user_serializer = UserSerializers(data={
    #         'username':attrs['name'],
    #         'email':attrs['email'],
    #         'password':'testpassword'
    #     })
    #     user_serializer.is_valid(raise_exception=True)
    #     attrs['user'] = user_serializer 
        
    #     return attrs
    
    @transaction.atomic
    def create(self, validated_data):
        # return super().create(validated_data)
        # user = validated_data['user'].save()
        user,_ = User.objects.get_or_create(
            email = validated_data['email'],
            defaults={
                'username' : validated_data['email'].split('@')[0],
                'first_name' : validated_data['name'].split(' ')[0],
            }
        )
        
        subscriber, _ = Subscriber.objects.get_or_create(
            user = user,
            defaults={
                'phone_number': validated_data['phone_number']
            }
        )

        subscription_serializer = SubscriptionSerializer(data={
            'plan':validated_data['plan_id'],
            'subscriber':subscriber.id,
        })
        subscription_serializer.is_valid(raise_exception=True)
        subscription = subscription_serializer.save()
        print(f'this is final sub: {subscription}')
        
        return subscription
    
    def to_representation(self, instance):
        return SubscriptionSerializer(instance).data


