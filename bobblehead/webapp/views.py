from django.shortcuts import render
# from django.views.generic.edit import View, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.http import HttpResponse
from webapp.models import Project, Tag
from django.http import Http404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import ProjectForm

# User management imports
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required





def index(request):
    """ Main page. """
    print "inside index"
    print "The session object is: ", request.session.items()
    if not request.user.is_authenticated():
        return render(request, 'user_profile/login_webapp.html')
    print("the user is: ", request.user.username)
    latest_project_list = Project.objects.order_by('posted')[:10]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'webapp/index.html', context)

    output = ', '.join([p.title for p in latest_project_list])
    return HttpResponse(output)


def request_meta(request):
    """ Return the meta itmes. """
    vl = request.META.items()
    vl.sort()
    html = []
    for k, v in vl:
        html.append('<tr><td>%s</td><td>%s</td>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def project_detail(request, project_id):
    """ Return the project details by project_id. """
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'webapp/details.html', {'project': project})


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
            prj_obj.user = request.user
            prj_obj.save()
            return HttpResponseRedirect('/webapp/' + str(prj_obj.id))
    else:
        form = ProjectForm()
    return render(request, 'webapp/create_project.html', {'form': form})


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
        print("inside the else, since we have a get request")
        return render(request, 'webapp/edit_project.html',
                      {'form': ProjectForm(instance=project),
                       'project': project})
    return render(request, 'webapp/details.html', {'project': project})


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


"""
def create_project(request):
    if request.method == 'GET':
        return render(request, 'webapp/create_project.html', {})
    elif request.method == 'POST':
        post = Project.objects.create(content=request.POST['content'],
                                     created_at=datetime.utcnow())
        # No need to call post.save() at this point -- it's already saved.
        return HttpResponseRedirect(reverse('project_detail', kwargs={'post_id': post.id}))
"""


# class project_create(View):
#     model = Project
#     #tags = Tag.objects.all()
#     fields = ['title', 'description', 'collaborators', 'category', 'articles', 'tags']

#     #fields = [ 'title', 'description' ]

#     def get(self, request):
#         tags = Tag.objects.all()
#         return render(request, 'webapp/project_form.html', {'tags': tags})

#     def post(self, request):
#         print request.POST
#         return HttpResponse()

# class project_update(UpdateView):
#     model = Project
#     fields = ['title', 'description', 'collaborators', 'category', 'articles','tags']

# class project_delete(DeleteView):
#     model = Project
#     success_url = reverse_lazy('project-list')

# #def create_project(request):
# #    """Description goes here"""
# #    request.POST['']
# #    p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
# #    return render (request, 'webapp/createproject.html', {''})

# def update_project(request):
#     """Description goes here"""

#     return None

# def delete_project(request):
#     """Description goes here"""

#     return None

# def create_user(request):
#     """Description goes here"""
#     return None

# def user_details(request, user_id):
#     """Description goes here"""
#     return None
