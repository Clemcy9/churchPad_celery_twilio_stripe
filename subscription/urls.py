from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('subscribe/', view=views.SubcriptionCreateView.as_view(), name='subscribe'),
    # path('subscriptions/')
    
]