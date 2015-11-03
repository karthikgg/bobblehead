from django.shortcuts import render
from user_profile.models import UserProfile
from user_profile.views import is_authenticated

from django.http import HttpResponseRedirect, HttpResponse

from .forms import CommentForm
from submissions.models import Submission
from django.core import serializers
from .models import Comment

import json


# Create your views here.
@is_authenticated()
def new_comment(request, sub_id):
    submission = Submission.objects.get(pk=sub_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_email = request.session['email']
            user = UserProfile.objects.get(email=user_email)
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.submission = submission
            comment.save()
            return HttpResponseRedirect('/submissions/show/' + str(sub_id))
        else:
            print "comment wasn't valid!"


@is_authenticated()
def comments_JSON(request, sub_id):
    """ Return a list of projects with only a
        select list of fields (as set by the fields param)
    """
    submission = Submission.objects.get(pk=sub_id)
    comments_as_json = serializers.serialize(
        'json',
        Comment.objects.filter(submission=submission),
        fields=('user',
                'posted',
                'content',
                'description',
                'pk'),
        use_natural_foreign_keys=True)
    return HttpResponse(json.dumps(comments_as_json), content_type='json')
