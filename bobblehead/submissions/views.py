from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404

from .models import Submission
from .forms import SubmissionForm

from webapp.models import Project
from user_profile.models import UserProfile

from user_profile.views import is_authenticated


@is_authenticated()
def new_submission(request, project_id):
    project = Project.objects.get(pk=project_id)
    user_profile = UserProfile.objects.get(email=request.session['email'])
    if request.method == "POST":
        submission_form = SubmissionForm(request.POST)
        if submission_form.is_valid():
            submission = submission_form.save(commit=False)
            submission.project = project
            submission.save()
            submission.members.add(user_profile)
            submission.save()
            return HttpResponseRedirect('/webapp/' + str(project_id))
    else:
        submission_form = SubmissionForm()
        return render(request, 'submissions/new_submission.html', {'form': submission_form, 'project_id':project_id})
