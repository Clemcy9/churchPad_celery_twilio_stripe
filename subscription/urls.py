from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('subscribe/', view=views.SubscriptionCreateView.as_view(), name='subscribe'),
    path('subscription/', view=views.SubcriptionListView.as_view(), name='subscriptions'),
    path('unsubscribe/<int:pk>', view=views.SubscriptionDeleteView.as_view(), name='unsubscribe')
    
]