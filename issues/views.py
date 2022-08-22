from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Issue
from .forms import IssueForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

class IssueListView(ListView):
    model = Issue
    template_name = 'issues.html'

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'

class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issue_create.html'
    fields = ['issue_name', 'body', 'created_by']

class IssueUpdateView(UpdateView):
    model = Issue
    template_name = 'issue_edit.html'
    fields = ['issue_name', 'body']

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue_delete.html'
    success_url = reverse_lazy('issues')

# def list_view(request):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}

#     # add the dictionary during initialization
#     context["dataset"] = Issue.objects.all()
            
#     return render(request, "issues.html", context)

# def create_view(request):
#     context = {}

#     form = IssueForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context['form'] = form

#     return render(request, "create_issue.html", context)