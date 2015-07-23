from django.shortcuts import render
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView
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

def login_webapp(request):
    """ View to log in user. """
    username = request.POST['username']
    password = request.POST['password']
    print username, password
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/webapp/')
        else:
            print("user logged in is not active")
    else:
        print("no user!")
        return render(request, 'webapp/login_webapp.html')
    return render(request, 'webapp/index.html')

# @login_required(login_url='/webapp/login_webapp')
def index(request):
    """ Main page. """
    print "inside index"
    if not request.user.is_authenticated():
        return render(request, 'webapp/login_webapp.html')

    latest_project_list = Project.objects.order_by('posted')[:10]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'webapp/index.html', context)

    output = ', '.join([p.title for p in latest_project_list])
    return HttpResponse(output)

def request_meta(request):
    vl = request.META.items()
    vl.sort()
    html = []
    for k,v in vl:
        html.append('<tr><td>%s</td><td>%s</td>' %(k,v))
    return HttpResponse ('<table>%s</table>' % '\n'.join(html))

def project_detail(request, project_id):
    """Description goes here"""
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404 ("Project does not exist")
    return render (request, 'webapp/details.html', {'project': project})

def create_project(request):
    if request.method == "POST":

        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            m = form.save()
            return HttpResponseRedirect('/webapp/'+str(m.id))
    else:
        form = ProjectForm()
    return render(request, 'webapp/my_template.html', {'form': form})

def edit_project(request, project_id):
    print("inside edit_project")
    try:
        project = Project.objects.get(pk=project_id)
        print ("the project is: ", project.title)
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
        #grab project
        print("inside the else, since we have a get request")
        return render(request, 'webapp/edit_project.html', {'form': ProjectForm(instance=project), 'project': project})
    return render(request, 'webapp/details.html', {'project': project})
    #pass it into forms
    #form = ProjectUpdate(request.GET)

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

class project_create(View):
    model = Project
    #tags = Tag.objects.all()
    fields = ['title', 'description', 'collaborators', 'category', 'articles', 'tags']

    #fields = [ 'title', 'description' ]

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'webapp/project_form.html', {'tags': tags})

    def post(self, request):
        print request.POST
        return HttpResponse()

class project_update(UpdateView):
    model = Project
    fields = ['title', 'description', 'collaborators', 'category', 'articles','tags']

class project_delete(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')

#def create_project(request):
#    """Description goes here"""
#    request.POST['']
#    p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
#    return render (request, 'webapp/createproject.html', {''})

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
