from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
# from django.contrib.auth.forms import UserCreationForm
# from webapp.models import Project
from django.contrib.auth import logout
from .forms import UserProfileForm
from .models import UserProfile

from webapp.models import Project, CATEGORY_CHOICES
from submissions.models import Submission

# OpenID imports
from openid.consumer import consumer
# The standard openID formats to ask for user info, sreg is specific to openid provider
from openid.extensions import ax, sreg
from functools import wraps

from config import openid_settings

def is_authenticated():
    """ Decorator to check if user is authenticated """
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            # print "There are the arguments: ", kwargs
            # request = kwargs['request']
            if 'udacity_key' in request.session:
                return func(request, *args, **kwargs)
            else:
                return render(request, 'user_profile/login_webapp.html')
        return wrapper
    return decorator


def logout_webapp(request):
    """ Log the user out """
    if request.user and 'udacity_key' not in request.session:
        # If the user was authenticated locally
        logout(request)
    else:
        # If the user was authenticated using Udacity
        try:
            del request.session['udacity_key']
            del request.session['email']
            del request.session['name']
        except KeyError:
            pass
    return HttpResponseRedirect('/webapp')


def login_webapp(request):
    """ View to log in user. """
    # print "The session is: ", request.session
    # username = request.POST['username']
    # password = request.POST['password']
    # print username, password
    # user = authenticate(username=username, password=password)
    print "in login webapp: ", request.session
    if 'email' in request.session:
        print "User: ", request.session['email']
        # if user.is_active:
        #     login(request, user)
        #     request.session['email'] = user.email
        return HttpResponseRedirect('/webapp/')
        # else:
        #     print("user logged in is not active")
    else:
        print("no user!")
        return render(request, 'user_profile/login_webapp.html')
    return render(request, 'webapp/index.html')


# def create_profile(request):
#     """ Create profile if not exists. """
#     if request.method == "POST":
#         form_user = UserForm(request.POST)
#         form_profile = UserProfileForm(request.POST)
#         if form_user.is_valid() and form_profile.is_valid():
#             # Save the user information first
#             user = form_user.save()
#             # m.set_password(m.password)
#             # Save the profile related information later, and add user
#             profile = form_profile.save(commit=False)
#             profile.user = user
#             profile.email = user.email
#             profile.udacity_key = ""
#             profile.save()
#             return HttpResponseRedirect('/webapp/')
#         else:
#             print "form was invalid!"
#     else:
#         form_user = UserForm()
#         form_profile = UserProfileForm()
#     # return HttpResponse("Create User Profile Here")
#     return render(request, 'user_profile/create_profile.html',
#                   {'form_user': form_user, 'form_profile': form_profile})


@is_authenticated()
def edit(request):
    """ Edit the user's own profile """
    try:
        user_profile = UserProfile.objects.get(email=request.session['email'])
    except UserProfile.DoesNotExist:
        raise Http404("User does not exist/is not signed in")
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        # check whether it's valid:
        if form.is_valid():
            m = form.save()
            m.save()
            return HttpResponseRedirect('/user_profile/show/' + user_profile.email)
    else:
        return render(request, 'user_profile/edit_profile.html',
                      {'form': UserProfileForm(instance=user_profile), 'user_profile': user_profile, 'nanodegree_choices':UserProfile.NANODEGREE_CHOICES},)


@is_authenticated()
def show(request, email):
    """ Show user's profile, and the project's they have created. """
    try:
        user_profile = UserProfile.objects.get(email=email)
        projects_list = Project.objects.filter(user=user_profile)
        # Return all submissions that the user has made.
        submissions_list = Submission.objects.filter(members__in=[user_profile])
    except UserProfile.DoesNotExist:
        print "User Does not exist!"
        raise Http404("User doesnt exist")
    return render(request, 'user_profile/show_profile.html', {'user_profile': user_profile, 'projects': projects_list, 'submissions_list': submissions_list})


def login_udacity(request):
    """ Authenticate with Udacity using OpenID """
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
        ax_request.add(ax.AttrInfo('http://openid.net/schema/person/guid',
                                   required=True,))

        auth_request.addExtension(ax_request)

        realm_url = openid_settings.REALM_URL
        return_url = openid_settings.RETURN_URL

        udacity_url = auth_request.redirectURL(realm_url, return_url)
        return HttpResponseRedirect(udacity_url)


def udacity_user(request):
    """ Callback function for authentication with Udacity. """
    cons_obj = consumer.Consumer(request.session, None)
    path = openid_settings.RETURN_URL
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
        # Store items returned from Udacity in the session object
        for key in sreg_items:
            request.session[key] = sreg_items[key]
        for key in ax_items:
            request.session[key] = ax_items[key]

        print "the session object is: ", request.session
        if not UserProfile.objects.filter(udacity_key=request.session['udacity_key']).exists():
            # base_user = User(username=request.session['email'],
            #                  email=request.session['email'])
            # base_user.backend = "udacity"
            # base_user.save()
            user_profile = UserProfile(email=request.session['email'],
                                       nickname=request.session['name'],
                                       udacity_key=request.session['udacity_key'])

            user_profile.save()
        # user_profile.user(email=email=request.session['email'])
    else:
        print "Nope"
    return HttpResponseRedirect('/webapp/')
