from django.shortcuts import render
from . models import portfolio_project

def home(request):
    projects = portfolio_project.objects.all()
    return render(request, 'portfolio_app/base.html', {'projects':projects})