from django.contrib import admin
from .models import Plan, Subscriber, Subscription
# Register your models here.

admin.site.register([Plan, Subscriber, Subscription])