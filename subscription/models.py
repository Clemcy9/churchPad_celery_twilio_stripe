from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
plan_choices = (
    ('basic', 'basic'),
    ('standard', 'standard'),
    ('premuim', 'premuim')
)
class Plan(models.Model):
    name = models.CharField(max_length=100, choices=plan_choices)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name + 'plan'

class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    plan = models.ForeignKey(Plan, blank=True, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + str(self.plan) + str(self.created_on)

