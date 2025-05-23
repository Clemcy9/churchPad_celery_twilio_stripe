from django.urls import path, include
from .views import CreateUserView, CreateTokenView, ManageUserView

app_name = 'account'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me')
]