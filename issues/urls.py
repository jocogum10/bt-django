from django.urls import path
from .views import home, IssueListView

urlpatterns = [
  path('', home, name='home'),
  path('issues/', IssueListView.as_view(),name='issues')
]