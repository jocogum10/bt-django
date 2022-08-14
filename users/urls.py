from django.urls import path, include
from .views import users

urlpatterns = [
    path('', users, name='users'),
    path('', include('django.contrib.auth.urls'))
]