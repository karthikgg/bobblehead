from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from webapp.models import Project
from django.http import Http404

def index(request):
    """Description goes here"""
    latest_project_list = Project.objects.order_by('posted')[:10]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'webapp/index.html', context)

    output = ', '.join([p.title for p in latest_project_list])
    return HttpResponse(output)

def project_detail(request, project_id):
    """Description goes here"""
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404 ("Project does not exist")
    return render (request, 'webapp/details.html', {'project': project})


def create_project(request):
    """Description goes here"""
    return render (request, 'webapp/createproject.html', context)

def update_project(request):
    """Description goes here"""

    return None

def delete_project(request):
    """Description goes here"""

    return None

def create_user(request):
    """Description goes here"""
    return None

def user_details(request, user_id):
    """Description goes here"""
    return None
