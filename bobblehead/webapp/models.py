""" Models for webapp - project, tags. """

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from user_profile.models import UserProfile

CATEGORY_CHOICES = [('STUDENT', 'Student Project'),
                    ('UDACITY', 'Udacity Project'),
                    ('ENTERPRISE', 'Enterprise Project'),
                    ('OPEN SOURCE', 'Open Source'),
                    ('CONTEST', 'Contest')]

DIFFICULTY_LEVEL = [('EASY', 'Easy'),
                    ('MEDIUM', 'Medium'),
                    ('HARD', 'Hard')]


class Tag(models.Model):

    """ Projects are tagged for classification. """

    tag_name = models.CharField(max_length=200)

    def __unicode__(self):
        """ Return the tag name to better identify object. """
        return self.tag_name


class Project(models.Model):

    """ Project class - all information about projects. """
    # user = models.OneToOneField(UserProfile, default=None)
    user = models.ForeignKey(UserProfile, default=None)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    collaborators = models.IntegerField(default=1)
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.CharField(max_length=15,
                                choices=CATEGORY_CHOICES,
                                default='STUDENT')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVEL, default=1)
    articles = models.CharField(max_length=5000)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        """ Return the absolute URL for the project, by id. """
        return reverse('project-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        """ Return the project title to better identify object. """
        return self.title


class TagsProject (models.Model):

    """ Tags connected to set of project """

    tag = models.ForeignKey(Tag)
    project = models.ForeignKey(Project)
