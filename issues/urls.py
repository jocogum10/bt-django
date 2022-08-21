from django.urls import path
from .views import home, list_view, create_view

urlpatterns = [
  path('', home, name='home'),
  path('issues/', list_view,name='issues'),
  path('issues/create', create_view, name='create')
]