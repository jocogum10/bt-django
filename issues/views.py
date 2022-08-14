from django.shortcuts import render
from django.views.generic import ListView
from .models import Issue

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

class IssueListView(ListView):
    model = Issue
    template_name = 'issues.html'