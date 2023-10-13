from django.shortcuts import render
from projects.models import Project as proj
from projects.models import AboutEducation as edu
from projects.models import AboutExperience as exp
from projects.models import AboutSkills as sk
from projects.models import AboutLanguages as lan
from projects.models import AboutInterests as intr

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
    about_edu = edu.objects.all()
    about_exp = exp.objects.all()
    about_proj = proj.objects.all()
    about_skills = sk.objects.all()
    about_languages = lan.objects.all()
    about_interests = intr.objects.all()

    return render(request, 'projects/about.html',
                  {'education' : about_edu,
                   'experience' : about_exp,
                   'projects' : about_proj,
                   'skills' : about_skills,
                   'languages' : about_languages,
                   'interests' : about_interests
                   }
                  )

def contact(request):
    return render(request, 'projects/contact.html')

def download(request):
    return render(request, 'projects/download.html')

def project_detail(request, pk):
    projects = proj.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', 
                  {'projects' : projects}
                  )