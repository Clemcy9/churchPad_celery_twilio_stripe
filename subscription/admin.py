from django.contrib import admin
from .models import Plan, Subscriber, Subscription
# Register your models here.

class SubscriptionInline(admin.StackedInline):  
    model = Subscription
    extra = 1  

class SubscriberAdmin(admin.ModelAdmin):
    inlines =[SubscriptionInline]

admin.site.register([Plan, Subscription])
admin.site.register(Subscriber,SubscriberAdmin)