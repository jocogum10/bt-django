from django.urls import path
from .views import home, IssueCreateView, IssueDetailView, IssueListView, IssueUpdateView, IssueDeleteView

urlpatterns = [
  path('', home, name='home'),
  # path('issues/', list_view,name='issues'),
  # path('issues/create', create_view, name='create')
  path('issues/', IssueListView.as_view(), name='issues'),
  path('issues/create', IssueCreateView.as_view(), name='issue_create'),
  path('issues/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
  path('issues/<int:pk>/edit', IssueUpdateView.as_view(), name='issue_edit'),
  path('issues/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete')
]