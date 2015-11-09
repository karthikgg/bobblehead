from django.db import models
from projects.models import Project
from user_profile.models import UserProfile
from comments.models import Comment


class Submission(models.Model):

    """ project submission details """
    # project object
    project = models.ForeignKey(Project)
    # URLField defaults to 200 max length, to hold submission link
    link = models.URLField()
    # The user who adds the submission is automatically added
    members = models.ManyToManyField(UserProfile)
    comments = models.ManyToManyField(Comment)
    description = models.TextField()


    def __unicode__(self):
        """ Return the tag name to better identify object. """
        return self.project.title
