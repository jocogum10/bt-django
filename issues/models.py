from django.db import models
from django.urls import reverse

# Create your models here.
class Issue(models.Model):
    issue_name = models.CharField(max_length=200)
    body = models.TextField()
    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.issue_name

    def get_absolute_url(self):
        return reverse("issue_detail", kwargs={"pk": self.pk})