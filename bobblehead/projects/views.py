from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project, Tag, Articles
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core import serializers

from .forms import ProjectForm

from user_profile.views import is_authenticated
from user_profile.models import UserProfile

from submissions.models import Submission

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
        "property": "tags",
        "value": "there"
    },
    {
        "type": "filter",
        "property": "user",
        "value": "pshevade@gmail.com"
    }
]


@is_authenticated()
def projects_JSON(request):
    """ Return a list of projects with only a
        select list of fields (as set by the fields param)
    """
    projects_as_json = serializers.serialize(
        'json',
        Project.objects.all(),
        fields=('title',
                'posted',
                'difficulty',
                'tags',
                'articles',
                'user',
                'description',
                'pk'),
        use_natural_foreign_keys=True)
    return HttpResponse(json.dumps(projects_as_json), content_type='json')


@is_authenticated()
def tags_JSON(request):
    """ Return a list of all tags. """
    tags_as_json = serializers.serialize('json', Tag.objects.all())
    return HttpResponse(json.dumps(tags_as_json), content_type='json')


def _get_projects(filters):
    """ Return projects based on a query set """
    # First order the objects, so separate that out
    orders_query = [o for o in filters if o['type']=='order']
    # Filter objects next, so separate those out
    filters_query = [f for f in filters if f['type']=='filter']

    projects = Project.objects.all()
    # We need a dictonary to pass to Django's filter function
    query_dict = {}
    # Order the projects based on the ordering queries
    for orders in orders_query:
        projects = projects.order_by(orders['property'])
    # create the dictonary based on the filtering queries
    for filters in filters_query:
        # First, if we want to filter by user, find the user
        if filters['property'] =='user':
            try:
                user_p = UserProfile.objects.get(email=filters['value'])
                query_dict[filters['property']] = user_p
            except UserProfile.DoesNotExist:
                raise Http404("User does not exist")
        # Second, if the filter is by tags, change the query phrase
        # to 'tags__tag_name' - this is because tags is a ManyToManyField
        # and we want to search by the tag_name property of Tag objects
        elif filters['property'] == 'tags':
            filters['property'] = 'tags__tag_name'
            query_dict[filters['property']] = filters['value']
        else:
            # Make a dictionary, property: value, and you can pass it to filter fn
            query_dict[filters['property']] = filters['value']
    projects = projects.filter(**query_dict)
    return projects


@is_authenticated()
def query_projects(request):
    """ Return projects based on a set of filters.
        Filters will be JSON object and passed through request """
    try:
        filters = request.data
    except AttributeError:
        filters = FILTER
    projects = _get_projects(filters)
    projects_as_json = serializers.serialize('json', projects)
    return HttpResponse(json.dumps(projects_as_json), content_type='json')


@is_authenticated()
def index(request):
    """ Main page. """
    user_profile = UserProfile.objects.get(email=request.session['email'])
    latest_project_list = Project.objects.order_by('posted')[:10]
    context = {'latest_project_list': latest_project_list, 'user_profile': user_profile}
    return render(request, 'projects/index.html', context)


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
        user_profile = UserProfile.objects.get(email=request.session['email'])
        submissions_list = Submission.objects.filter(project=project)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    context = {'project': project, 'submissions_list':submissions_list, 'current_user': request.session['email'], 'user_profile': user_profile}
    return render(request, 'projects/details.html', context)


@is_authenticated()
def create_project(request):
    """ Create project from user input.

    GET: Return the form to create a project.
    POST: Create a new project and redirect to the project details
    """
    if request.method == "POST":
        temp = json.loads(request.body)
        form = ProjectForm(temp)

        # check whether it's valid:
        if form.is_valid():
            prj_obj = form.save(commit=False)
            # fint the user profile object based on the email in session
            user_profile = UserProfile.objects.get(email=request.session['email'])
            prj_obj.user = user_profile
            # Save the project object - project needs to exist before
            # manytomany field is accessed.
            prj_obj.save()
            # get the list of tag objects to add to project
            tag_objects_list = _get_tags(form.cleaned_data['tags_list'])
            article_object_list = _get_articles(form.cleaned_data['articles'])
            for tag_object in tag_objects_list:
                prj_obj.tags.add(tag_object)
            for article_object in article_object_list:
                prj_obj.articles.add(article_object)
            prj_obj.save()
            return HttpResponse(str(prj_obj.id))
            # return HttpResponseRedirect('/projects/' + str(prj_obj.id))
        else:
            print form.errors.as_data()
    else:
        # Remove when front end updated.
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})


def _get_tags(tag_string):
    """ Take the string of tags, and convert into tags object
        If tags already exist, dont create.
        Return a list of tag objects to add to the project
    """
    tag_objects_list = []
    # remove all whitespaces
    tag_string_cleaned = tag_string.replace(" ", "")
    tokens = tag_string_cleaned.split(',')
    for tok in tokens:
        try:
            tag_object = Tag.objects.get(tag_name=tok)
        except Tag.DoesNotExist:
            tag_object = Tag(tag_name=tok)
            tag_object.save()
        if tag_object not in tag_objects_list:
            tag_objects_list.append(tag_object)
    return tag_objects_list


def _get_articles(article_string):
    """ Take the string of articles, and convert into articles object
        If article already exist, dont create.
        Return a list of article objects to add to the project
    """
    article_objects_list = []
    # remove all whitespaces
    article_string_cleaned = article_string.replace(" ", "")
    tokens = article_string_cleaned.split(',')
    for tok in tokens:
        try:
            article_object = Articles.objects.get(url=tok)
        except Articles.DoesNotExist:
            article_object = Articles(url=tok)
            article_object.save()
        if article_object not in article_objects_list:
            article_objects_list.append(article_object)
    return article_objects_list


@is_authenticated()
def edit_project(request, project_id):
    """ Edit project based on user input.

    GET: Return the form with project details entered
    POST: Edit the existing project with new details
    """
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    # check whether the user is the one who created this project
    
    if project.user.email != request.session['email']:
        return HttpResponseRedirect('/projects/'+str(project_id))
    else:
        if request.method == "POST":
            temp = json.loads(request.body)
            form = ProjectForm(temp, instance=project)
            # form = ProjectForm(request.POST, instance=project)
            # check whether it's valid:
            if form.is_valid():
                #clear any previously stored tags to fix the bug 
                #where we remove the tags and its not reflected
                try:
                    project.tags.clear()
                    project.articles.clear()
                except:
                    pass
                m = form.save(commit=False)
                m.save()
                tag_objects_list = _get_tags(form.cleaned_data['tags_list'])
                article_object_list = _get_articles(form.cleaned_data['articles'])
                for tag_object in tag_objects_list:
                    m.tags.add(tag_object)
                for article_object in article_object_list:
                    m.articles.add(article_object)
                m.save()
                # return HttpResponseRedirect('/projects/' + str(m.id))
                # return project_detail(request, m.id)
                return HttpResponse(str(m.id))
            else:
                return render(request, 'projects/edit_project.html',
                              {'project': project})
                # return render(request, 'projects/error_edit.html', {'form': form})
        else:
            return render(request, 'projects/edit_project.html',
                          {'project': project})
    return project_detail(request, project_id)


@is_authenticated()
def delete_project(request, project_id):
    """ Delete a project based on user input.

    GET: Return the form with project details entered
    POST: Delete the existing project with new details
    """
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    # check whether the user is the one who created this project
    if project.user.email != request.session['email']:
        return HttpResponseRedirect('/projects/' + str(project_id))
    else:
        if request.method == "POST":
            if project:
                project.delete()
                return HttpResponseRedirect('/projects/')
            else:
                return render(request, 'projects/delete_project.html',
                              {'project': project})
    return render(request, 'projects/delete_project.html', {'project': project})
