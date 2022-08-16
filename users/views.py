from django.shortcuts import render

# Create your views here.
def users(request):
    context = {}
    return render(request, 'users.html', context=context)