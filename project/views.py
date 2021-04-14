from django.shortcuts import render, get_object_or_404
from .models import Project,Certificate

# Create your views here.
def index(request):
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'projects':projects,
        'certificates':certificates
    }
    
    return render(request, 'project/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'project':project
    }
    return render(request, 'project/detail.html', context)
    
    
def cer_detail(request,project_id):
    certificate = get_object_or_404(Certificate, id=project_id)
    context = {
        'certificate':certificate
    }
    return render(request,'project/cer_detail.html',context)
