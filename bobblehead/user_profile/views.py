from django.shortcuts import render
from django.http import HttpResponseRedirect

# from django.contrib.auth.forms import UserCreationForm
# from webapp.models import Project

from .forms import UserProfileForm, UserForm

# OpenID imports
from openid.consumer import consumer
# The standard openID formats to ask for user info, sreg is specific to openid provider
from openid.extensions import ax, sreg


def login_webapp(request):
    """ View to log in user. """
    print "The session is: ", request.session
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
        return render(request, 'user_profile/login_webapp.html')
    return render(request, 'webapp/index.html')

# Create your views here.
def create_profile(request):
    """ Create profile if not exists. """

    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST)
        if form_user.is_valid() and form_profile.is_valid():
            # Save the user information first
            user = form_user.save()
            # m.set_password(m.password)
            # Save the profile related information later, and add user
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect('/webapp/')
        else:
            print "form was invalid!"
    else:
        form_user = UserForm()
        form_profile = UserProfileForm()
    # return HttpResponse("Create User Profile Here")
    return render(request, 'user_profile/create_profile.html',
                  {'form_user': form_user, 'form_profile': form_profile})


def login_udacity(request):
    if request.method == "POST":
        cons_obj = consumer.Consumer(request.session, None)
        openid_url = "https://www.udacity.com/openid"
        auth_request = cons_obj.begin(openid_url)

        # extending the reuqest object
        sreg_request = sreg.SRegRequest(
            required=['fullname', 'email', 'nickname'],
            )
        auth_request.addExtension(sreg_request)

        # To request for getting user_id @ udacity
        ax_request = ax.FetchRequest()
        # The url is associated with the user_id format at udacity
        ax_request.add(ax.AttrInfo('http://openid.net/schema/person/guid',required=True,))

        auth_request.addExtension(ax_request)

        realm_url = 'http://localhost:8000/'
        return_url = 'http://localhost:8000/user_profile/udacity_user'

        udacity_url = auth_request.redirectURL(realm_url, return_url)
        return HttpResponseRedirect(udacity_url)

def udacity_user(request):
    cons_obj = consumer.Consumer(request.session, None)
    path = "http://localhost:8000/user_profile/udacity_user"
    the_response = cons_obj.complete(request.GET, path)


    if the_response.status == consumer.SUCCESS:
        # Gather Info from Udacity
        sreg_response = sreg.SRegResponse.fromSuccessResponse(the_response)
        if sreg_response:
            sreg_items = {
                'email': sreg_response.get('email'),
                'name': sreg_response.get('nickname'),
            }
        ax_response = ax.FetchResponse.fromSuccessResponse(the_response)
        if ax_response:
            ax_items = {
                'udacity_key': ax_response.get('http://openid.net/schema/person/guid')[0],
            }
            
        for key in sreg_items:
            request.session[key] = sreg_items[key]
            
        for key in ax_items:
            request.session[key] = ax_items[key]
        return HttpResponseRedirect('/webapp/')
    else:
        print "Nope"
        return HttpResponseRedirect('/webapp/')
