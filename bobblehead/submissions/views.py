# HTTP imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404

# Submission models, forms
from .models import Submission
from .forms import SubmissionForm

# External App models, views
from projects.models import Project
from user_profile.models import UserProfile
from user_profile.views import is_authenticated
import markdown
import bleach
from comments.forms import CommentForm
from comments.models import Comment


@is_authenticated()
def _add_members_to_submission(request, member_emails, submission):
    """ add members to the submission, if they exist.
        TODO: in the future, create a profile for the email address, even if
        the user hasn't ever logged in?
        We need to pass "request" for the is_authenticated decorator to work
    """
    for email in member_emails:
        try:
            member_profile = UserProfile.objects.get(email=email.strip())
            submission.members.add(member_profile)
        except UserProfile.DoesNotExist:
            pass
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
            submission = submission_form.save(commit=False)
            submission.description = bleach.clean(submission.description, strip=True)
            submission.project = project
            submission.save()
            _add_members_to_submission(request, member_emails, submission)
            return HttpResponseRedirect('/projects/' + str(project_id))
        else:
            print submission_form.errors
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
        submission.description = markdown.markdown(submission.description, extensions=['markdown.extensions.fenced_code'])
        #comment_list = submission.comments.order_by('-posted')
        # print "This submissions has the following comments:" 
        comments_list = []
        for comment in submission.comments.order_by('-posted'):
            comment.content = markdown.markdown(comment.content, extensions=['markdown.extensions.fenced_code'])
            comments_list.append(comment)
        #     print comment.content
    except Submission.DoesNotExist:
        raise Http404("Submission object not found")
    return render(request, 'submissions/show_submission.html', {'submission': submission, 'comments_list': comments_list, 'user_email':request.session['email']})


@is_authenticated()
def add_new_comment(request, submission_id):
    submission = Submission.objects.get(pk=submission_id)
    # problem = Problem.objects.get(pk=problem_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content = bleach.clean(comment.content, strip=True)
            comment.user = UserProfile.objects.get(email=request.session['email'])
            comment.save()
            submission.comments.add(comment)
        else:
            print comment_form.errors
            raise Http404('Form is not valid')
    comments_list = []
    for comment in submission.comments.order_by('-posted'):
        comment.content = markdown.markdown(comment.content, extensions=['markdown.extensions.fenced_code'])
        comments_list.append(comment)
    submission.description = markdown.markdown(submission.description, extensions=['markdown.extensions.fenced_code'])
    context = {'submission': submission, 'comments_list': comments_list, 'user_email':request.session['email']}
    # return render(request, 'submissions/show_submission.html', context)
    return HttpResponseRedirect('/submissions/show/' + str(submission_id))


@is_authenticated()
def edit_comment(request, sub_id, comment_id):
    submission = Submission.objects.get(pk=sub_id)
    try:
        comment = Comment.objects.get(pk=comment_id)
        if comment.user.email != request.session['email']:
            return HttpResponseRedirect('/submissions/show/'+str(sub_id))
    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = UserProfile.objects.get(email=request.session['email'])
            # comment.content = bleach.clean(comment.content, strip=True)
            print "Comment post bleach: ", comment.content
            # comment.content = markdown.markdown(comment.content)
            print "this is the comment content: ", comment.content
            comment.save()
            submission.comments.add(comment)
            return HttpResponseRedirect('/submissions/show/' + str(sub_id))
        else:
            print "comment wasn't valid!"
            print comment_form.errors
    elif request.method == 'GET':
        c_edit = comment
        # c_edit.content = bleach.clean(c_edit.content, strip=True)
        comment_form = CommentForm(instance=c_edit)

        return render(request, 'submissions/edit_comment.html',
                      {'form': comment_form, 'sub_id': sub_id, 'comment':comment})


@is_authenticated()
def delete_comment(request, sub_id, comment_id):
    try:
        submission = Submission.objects.get(pk=sub_id)
        comment = Comment.objects.get(pk=comment_id)
        if comment.user.email != request.session['email']:
            return HttpResponseRedirect('/submissions/show/'+str(sub_id))
        submission.comments.remove(comment)
        comment.delete()

    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")
    return HttpResponseRedirect('/submissions/show/'+str(sub_id))
