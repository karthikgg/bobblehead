from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Tag
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core import serializers

from .models import Problem, Solution
from .forms import ProblemForm, SolutionForm
from user_profile.views import is_authenticated
from user_profile.models import UserProfile

from comments.forms import CommentForm

import projects
import json

import bleach
import markdown

# @is_authenticated()
# def problems_JSON(request):
#     """ Return a list of projects with only a
#         select list of fields (as set by the fields param)
#     """
#     projects_as_json = serializers.serialize(
#         'json',
#         Problem.objects.all(),
#         fields=('title',
#                 'posted',
#                 'difficulty',
#                 'tags',
#                 'due_date',
#                 'link',
#                 'user',
#                 'description',
#                 'pk'),
#         use_natural_foreign_keys=True)
#     return HttpResponse(json.dumps(projects_as_json), content_type='json')


# @is_authenticated()
# def tags_JSON(request):
#     """ Return a list of all tags. """
#     tags_as_json = serializers.serialize('json', Tag.objects.all())
#     return HttpResponse(json.dumps(tags_as_json), content_type='json')


# def _get_projects(filters):
#     """ Return projects based on a query set """
#     # First order the objects, so separate that out
#     orders_query = [o for o in filters if o['type']=='order']
#     # Filter objects next, so separate those out
#     filters_query = [f for f in filters if f['type']=='filter']

#     projects = Project.objects.all()
#     # We need a dictonary to pass to Django's filter function
#     query_dict = {}
#     # Order the projects based on the ordering queries
#     for orders in orders_query:
#         projects = projects.order_by(orders['property'])
#     # create the dictonary based on the filtering queries
#     for filters in filters_query:
#         # First, if we want to filter by user, find the user
#         if filters['property'] =='user':
#             try:
#                 user_p = UserProfile.objects.get(email=filters['value'])
#                 query_dict[filters['property']] = user_p
#             except UserProfile.DoesNotExist:
#                 raise Http404("User does not exist")
#         # Second, if the filter is by tags, change the query phrase
#         # to 'tags__tag_name' - this is because tags is a ManyToManyField
#         # and we want to search by the tag_name property of Tag objects
#         elif filters['property'] == 'tags':
#             filters['property'] = 'tags__tag_name'
#             query_dict[filters['property']] = filters['value']
#         else:
#             # Make a dictionary, property: value, and you can pass it to filter fn
#             query_dict[filters['property']] = filters['value']
#     projects = projects.filter(**query_dict)
#     return projects


# @is_authenticated()
# def query_projects(request):
#     """ Return projects based on a set of filters.
#         Filters will be JSON object and passed through request """
#     try:
#         filters = request.data
#     except AttributeError:
#         filters = FILTER
#     projects = _get_projects(filters)
#     projects_as_json = serializers.serialize('json', projects)
#     return HttpResponse(json.dumps(projects_as_json), content_type='json')


@is_authenticated()
def problems_list(request):
    """ List of all problems. """
    user_profile = UserProfile.objects.get(email=request.session['email'])
    latest_problems_list = Problem.objects.order_by('posted')[:10]
    print "The problems are: ", latest_problems_list
    context = {'latest_problems_list': latest_problems_list, 'user_profile': user_profile}
    return render(request, 'problems/problems_list.html', context)


@is_authenticated()
def problem_detail(request, problem_id):
    """ Return the project details by project_id. """
    try:
        problem = Problem.objects.get(pk=problem_id)
        problem.description = markdown.markdown(problem.description, extensions=['markdown.extensions.fenced_code'])
        user_profile = UserProfile.objects.get(email=request.session['email'])
        solutions_list = Solution.objects.filter(problem=problem)# need to add a way to get all answers to all questions here...
    except Problem.DoesNotExist:
        raise Http404("Project does not exist")
    context = {'problem': problem, 'current_user': request.session['email'], 'solutions_list':solutions_list}
    return render(request, 'problems/problem_detail.html', context)


@is_authenticated()
def new_problem(request):
    """ Create project from user input.

    GET: Return the form to create a project.
    POST: Create a new project and redirect to the project details
    """
    if request.method == "POST":
        # temp = json.loads(request.body)
        form = ProblemForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            problem = form.save(commit=False)
            # fint the user profile object based on the email in session
            user_profile = UserProfile.objects.get(email=request.session['email'])
            problem.user = user_profile
            problem.description = bleach.clean(problem.description, strip=True)
            # Save the project object - project needs to exist before
            # manytomany field is accessed.
            problem.save()
            # get the list of tag objects to add to project
            tag_objects_list = projects.views._get_tags(form.cleaned_data['tags_list'])
            for tag_object in tag_objects_list:
                print "this is the tag object: ", tag_object
                problem.tags.add(tag_object)
                print "this is the problem tags: ", problem.tags
            print "The problem object as created: ", problem.title, problem.tags
            problem.save()
            # return HttpResponse(str(problem.id))
            return HttpResponseRedirect('/problems/')
        else:
            print form.errors.as_data()
    else:
        # Remove when front end updated.
        form = ProblemForm()
    return render(request, 'problems/new_problem.html', {'form': form})


@is_authenticated()
def new_solution(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    if request.method == "POST":
        solution_form = SolutionForm(request.POST)
        if solution_form.is_valid():
            # print "The users line is: ", submission_form['members_list']
            solution = solution_form.save(commit=False)
            solution.description = bleach.clean(solution.description, strip=True)
            solution.problem = problem
            user_profile = UserProfile.objects.get(email=request.session['email'])
            solution.user = user_profile
            solution.save()
            return HttpResponseRedirect('/problems/' + str(problem_id))
        else:
            print solution_form.errors
            raise Http404('Form is not valid')

    else:
        solution_form = SolutionForm()
        return render(request, 'problems/new_solution.html', {'form': solution_form, 'problem_id': problem_id})


@is_authenticated()
def add_new_comment(request, solution_id, problem_id):
    solution = Solution.objects.get(pk=solution_id)
    problem = Problem.objects.get(pk=problem_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content = bleach.clean(comment.content, strip=True)
            comment.user = UserProfile.objects.get(email=request.session['email'])
            comment.save()
            solution.comments.add(comment)
        else:
            print comment_form.errors
            raise Http404('Form is not valid')
    problem.description = markdown.markdown(problem.description, extensions=['markdown.extensions.fenced_code'])
    solution = Solution.objects.get(pk=solution_id)
    comments_list = []
    for comment in solution.comments.order_by('-posted'):
        comment.content = markdown.markdown(comment.content, extensions=['markdown.extensions.fenced_code'])
        comments_list.append(comment)
    context = {'solution': solution, 'problem': problem, 'current_user': request.session['email'], 'comments_list':comments_list}
    return render(request, 'problems/show_solution.html', context)


@is_authenticated()
def show_solution(request, problem_id, solution_id):
    problem = Problem.objects.get(pk=problem_id)
    print "problem description is: ", problem.description
    problem.description = markdown.markdown(problem.description, extensions=['markdown.extensions.fenced_code'])
    print "problem description post markdown is: ", problem.description
    solution = Solution.objects.get(pk=solution_id)
    solution.description = markdown.markdown(solution.description, extransions=['markdown.extensions.fenced_code'])
    comments_list = []
    for comment in solution.comments.order_by('-posted'):
        comment.content = markdown.markdown(comment.content, extensions=['markdown.extensions.fenced_code'])
        comments_list.append(comment)
    context = {'solution': solution, 'problem': problem, 'current_user': request.session['email'], 'comments_list':comments_list}
    return render(request, 'problems/show_solution.html', context)



@is_authenticated()
def delete_problem(request, problem_id):
    pass


@is_authenticated()
def edit_problem(request, problem_id):
    pass
#     """ Edit project based on user input.

#     GET: Return the form with project details entered
#     POST: Edit the existing project with new details
#     """
#     try:
#         project = Project.objects.get(pk=project_id)
#     except Project.DoesNotExist:
#         raise Http404("Project does not exist")
#     # check whether the user is the one who created this project
    
#     if project.user.email != request.session['email']:
#         return HttpResponseRedirect('/projects/'+str(project_id))
#     else:
#         if request.method == "POST":
#             temp = json.loads(request.body)
#             form = ProjectForm(temp, instance=project)
#             # form = ProjectForm(request.POST, instance=project)
#             # check whether it's valid:
#             if form.is_valid():
#                 #clear any previously stored tags to fix the bug 
#                 #where we remove the tags and its not reflected
#                 try:
#                     project.tags.clear()
#                     project.articles.clear()
#                 except:
#                     pass
#                 m = form.save(commit=False)
#                 m.save()
#                 tag_objects_list = _get_tags(form.cleaned_data['tags_list'])
#                 article_object_list = _get_articles(form.cleaned_data['articles'])
#                 for tag_object in tag_objects_list:
#                     m.tags.add(tag_object)
#                 for article_object in article_object_list:
#                     m.articles.add(article_object)
#                 m.save()
#                 # return HttpResponseRedirect('/projects/' + str(m.id))
#                 # return project_detail(request, m.id)
#                 return HttpResponse(str(m.id))
#             else:
#                 return render(request, 'projects/edit_project.html',
#                               {'project': project})
#                 # return render(request, 'projects/error_edit.html', {'form': form})
#         else:
#             return render(request, 'projects/edit_project.html',
#                           {'project': project})
#     return project_detail(request, project_id)


# @is_authenticated()
# def delete_problem(request, problem_id):
#     """ Delete a project based on user input.

#     GET: Return the form with project details entered
#     POST: Delete the existing project with new details
#     """
#     try:
#         project = Project.objects.get(pk=project_id)
#     except Project.DoesNotExist:
#         raise Http404("Project does not exist")
#     # check whether the user is the one who created this project
#     if project.user.email != request.session['email']:
#         return HttpResponseRedirect('/projects/' + str(project_id))
#     else:
#         if request.method == "POST":
#             if project:
#                 project.delete()
#                 return HttpResponseRedirect('/projects/')
#             else:
#                 return render(request, 'projects/delete_project.html',
#                               {'project': project})
#     return render(request, 'projects/delete_project.html', {'project': project})
