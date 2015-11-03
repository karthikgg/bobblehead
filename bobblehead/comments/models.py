""" Models for projects - project, tags. """

from django.db import models
from user_profile.models import UserProfile
from submissions.models import Submission


class Comment(models.Model):

    """ Comment class - all information in a comment. """

    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, default=None)
    submission = models.ForeignKey(Submission, default=None)

    def __unicode__(self):
        """ Return the url """
        return str(self.posted) + ' by ' + self.user.nickname
