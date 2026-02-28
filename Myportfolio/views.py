from .models import Project
from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'Myportfolio/index.html', {
        'projects': projects
    })

def home(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'Myportfolio/index.html', {
        'projects': projects
    })
    

def reset_admin(request):
    user = User.objects.get(username='yourusername')
    user.set_password('newpassword123')
    user.save()
    return HttpResponse("Password Reset Done")