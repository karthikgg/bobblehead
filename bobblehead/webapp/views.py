from django.shortcuts import render
# from django.views.generic.edit import View, CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from webapp.models import Project
from django.http import Http404
from django.http import HttpResponseRedirect
from .forms import ProjectForm

from user_profile.views import is_authenticated
# User management imports
# from django.contrib.auth import authenticate, login
# from django.conf import settings
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required

from user_profile.models import UserProfile

from submissions.models import Submission

from django.core import serializers
import json

# Using this filter to test
FILTER = [
    {
        "type": "order",
        "property": "posted",
        "value": "a"
    },
    {
        "type": "filter",
        "property": "collaborators",
        "value": "1"
    },
    {
        "type": "filter",
        "property": "user",
        "value": "pshevade@gmail.com"
    }
]


@is_authenticated()
def projects_JSON(request):
    projects_as_json = serializers.serialize('json', Project.objects.all())
    return HttpResponse(json.dumps(projects_as_json), content_type='json')


def _get_projects(filters):
    orders_query = [o for o in filters if o['type']=='order']
    filters_query = [f for f in filters if f['type']=='filter']
    projects = Project.objects.all()
    query_dict = {}
    for orders in orders_query:
        projects = projects.order_by(orders['property'])
    for filters in filters_query:
        if filters['property'] =='user':
            # If the filter is over user, find the UserProfile object
            try:
                user_p = UserProfile.objects.get(email=filters['value'])
                query_dict[filters['property']] = user_p
            except UserProfile.DoesNotExist:
                raise Http404("User does not exist")
        else:
            # Make a dictionary, property: value, and you can pass it to filter fn
            query_dict[filters['property']] = filters['value']
    projects = projects.filter(**query_dict)
    # try:
    #     projects = projects.filter(**query_dict)
    # except Project.DoesNotExist:
    #     raise Http404("Project does not exist")
    return projects


@is_authenticated()
def query_projects(request):
    try:
        filters = request.data
        print "WE got data!"
    except AttributeError:
        filters = FILTER

    print "Reached query_projects fn, filters are: ", filters
    projects = _get_projects(filters)
    projects_as_json = serializers.serialize('json', projects)
    return HttpResponse(json.dumps(projects_as_json), content_type='json')


@is_authenticated()
def index(request):
    """ Main page. """
    print "inside index"
    # print "The session email is: ", request.session['email']
    # if request.user and 'udacity_key' not in request.session:
    #     print "The session user is: ", request.user
    #     if not request.user.is_authenticated():
    #         return render(request, 'user_profile/login_webapp.html')
    #     user_email = request.user.email
    # elif request.session['udacity_key']:
    #     user_profile = UserProfile.objects.get(email=request.session['email'])
    #     print("the user is: ", user_profile.email)
    # if is_authenticated(request):
    user_profile = UserProfile.objects.get(email=request.session['email'])
    latest_project_list = Project.objects.order_by('posted')[:10]
    context = {'latest_project_list': latest_project_list, 'user_profile': user_profile}
    return render(request, 'webapp/index.html', context)
    # else:
    #     return render(request, 'user_profile/login_webapp.html')


def request_meta(request):
    """ Return the meta itmes. """
    vl = request.META.items()
    vl.sort()
    html = []
    for k, v in vl:
        html.append('<tr><td>%s</td><td>%s</td>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


@is_authenticated()
def project_detail(request, project_id):
    """ Return the project details by project_id. """
    try:
        project = Project.objects.get(pk=project_id)
        submissions_list = Submission.objects.filter(project=project)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'webapp/details.html', {'project': project, 'submissions_list':submissions_list})


@is_authenticated()
def create_project(request):
    """ Create project from user input.

    GET: Return the form to create a project.
    POST: Create a new project and redirect to the project details
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            prj_obj = form.save(commit=False)
            user_profile = UserProfile.objects.get(email=request.session['email'])
            prj_obj.user = user_profile
            prj_obj.save()
            return HttpResponseRedirect('/webapp/' + str(prj_obj.id))
    else:
        pass
    return render(request, 'webapp/create_project.html')


@is_authenticated()
def edit_project(request, project_id):
    """ Edit project based on user input.

    GET: Return the form with project details entered
    POST: Edit the existing project with new details
    """
    try:
        project = Project.objects.get(pk=project_id)
        print("the project is: ", project.title)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        # check whether it's valid:
        if form.is_valid():
            m = form.save()
            m.save()
            return HttpResponseRedirect('/webapp/' + str(m.id))
    else:
        # grab project
        print "this is a form", ProjectForm(instance=project)
        print("inside the else, since we have a get request")
        return render(request, 'webapp/edit_project.html',
                      {'project': project})
    return render(request, 'webapp/details.html', {'project': project})


@is_authenticated()
def delete_project(request, project_id):
    """ Delete a project based on user input.

    GET: Return the form with project details entered
    POST: Delete the existing project with new details
    """
    try:
        project = Project.objects.get(pk=project_id)
        print("the project is: ", project.title)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    if request.method == "POST":
        # check whether it's valid:
        if project:
            project.delete()
            return HttpResponseRedirect('/webapp/')
    else:
        # grab project
        print("inside the else, since we have a get request")
        return render(request, 'webapp/delete_project.html',
                      {'project': project})
    return render(request, 'webapp/delete_project.html', {'project': project})
