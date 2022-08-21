from socket import fromshare
from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_name', 'body', 'created_by']