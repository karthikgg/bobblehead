from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from webapp.models import Project

def index(request):
    """Description goes here"""
    latest_project_list = Project.objects.order_by('posted')[:10]
    output = ', '.join([p.title for p in latest_project_list])
    return HttpResponse(output)

def project_detail(request, project_id):
    """Description goes here"""
    return None

def create_project(request):
    """Description goes here"""
    return None

def create_user(request):
    """Description goes here"""
    return None

def user_details(request, user_id):
    """Description goes here"""
    return None
