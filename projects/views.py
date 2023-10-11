from django.shortcuts import render
from projects.models import Project as proj

# Create your views here.
def home(request):
    return render(request, 'projects/index.html')

def projects(request):
    projects_obj = proj.objects.all()
    print(projects_obj)
    return render(request, 'projects/projects.html',
                   {'projects' : projects_obj}
                   )

def sign_up(request):
    return render(request, 'projects/sign_up.html')

def sign_in(request):
    return render(request, 'projects/sign_in.html')

def about(request):
    return render(request, 'projects/about.html')

def contact(request):
    return render(request, 'projects/contact.html')

def download(request):
    return render(request, 'projects/download.html')
