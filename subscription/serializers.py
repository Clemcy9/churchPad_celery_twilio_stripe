from rest_framework import serializers
from .models import Subscriber, Plan
from django.contrib.auth import get_user_model

User = get_user_model()

class SubscriberSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    plan_id = serializers.CharField()


    class Meta:
        model = Subscriber
        fields = ['phone_number', 'is_active']

    def create(self, validated_data):
        # return super().create(validated_data)
        name = validated_data.pop('name', None)
        email = validated_data.pop('email', None)
        plan_id = validated_data.pop('plan_id', None)

        try:
            plan = Plan.objects.get(id = plan_id)
            user = User.objects.create(
                first_name = name.split(' ')[0],
                email = email,
                username = email.split('@')[0]
            )
            return Subscriber.objects.create(user =user, plan=plan, **validated_data)
        except:
            msg = _('no plain with given id')
            raise serializers.ValidationError(msg, code='invalid credentials')
        