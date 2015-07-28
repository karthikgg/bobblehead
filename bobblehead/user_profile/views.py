from django.shortcuts import render
from django.http import HttpResponseRedirect

# from django.contrib.auth.forms import UserCreationForm
# from webapp.models import Project

from .forms import UserProfileForm, UserForm


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
