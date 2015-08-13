# HTTP imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404

# Submission models, forms
from .models import Submission
from .forms import SubmissionForm

# External App models, views
from webapp.models import Project
from user_profile.models import UserProfile
from user_profile.views import is_authenticated


@is_authenticated()
def _add_members_to_submission(request, member_emails, submission):
    """ add members to the submission, if they exist.
        TODO: in the future, create a profile for the email address, even if
        the user hasn't ever logged in?
        We need to pass "request" for the is_authenticated decorator to work
    """
    for email in member_emails:
        try:
            print "Here is the email: ", email
            member_profile = UserProfile.objects.get(email=email.strip())
            print member_profile.nickname
            submission.members.add(member_profile)
        except UserProfile.DoesNotExist:
            print "email doesn't exist - for future create a record"
    submission.save()


@is_authenticated()
def new_submission(request, project_id):
    """ Create a new submission entry """
    project = Project.objects.get(pk=project_id)
    if request.method == "POST":
        submission_form = SubmissionForm(request.POST)
        if submission_form.is_valid():
            # print "The users line is: ", submission_form['members_list']
            member_emails = [request.session['email']]
            member_emails.extend(submission_form.cleaned_data['members_list'].split(','))
            print "The member emails are: ", member_emails
            submission = submission_form.save(commit=False)
            submission.project = project
            submission.save()
            _add_members_to_submission(request, member_emails, submission)
            return HttpResponseRedirect('/webapp/' + str(project_id))
        else:
            raise Http404('Form is not valid')
    else:
        submission_form = SubmissionForm()
        return render(request, 'submissions/new_submission.html', {'form': submission_form, 'project_id': project_id})


@is_authenticated()
def show_submission(request, submission_id):
    """ Show a submission based on the id,
        usually redirects from project details page
    """
    try:
        submission = Submission.objects.get(pk=submission_id)
    except Submission.DoesNotExist:
        raise Http404("Submission object not found")
    return render(request, 'submissions/show_submission.html', {'submission': submission})
