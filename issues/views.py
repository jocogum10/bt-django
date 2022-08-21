from django.shortcuts import render
from django.views.generic import ListView
from .models import Issue
from .forms import IssueForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

# class IssueListView(ListView):
#     model = Issue
#     template_name = 'issues.html'

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = Issue.objects.all()
            
    return render(request, "issues.html", context)

def create_view(request):
    context = {}

    form = IssueForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form

    return render(request, "create_issue.html", context)