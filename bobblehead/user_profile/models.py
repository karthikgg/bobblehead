""" user_profiles - to display user's information """
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):

    """ User information. """

    user = models.OneToOneField(User)
    NANODEGREE_CHOICES = (('FULLSTACK', 'FullStack Developer'),
                          ('FRONTEND', 'Frontend Developer'),
                          ('ANDROID', 'Android Developer'),
                          ('DATA ANALYST', 'Data Analyst'),
                          ('IOS DEVELOPER', 'IOS Developer'),)
    nanodegree = models.CharField(max_length=15,
                                  choices=NANODEGREE_CHOICES,)

    def __unicode__(self):
        """ Return the username to better identify object. """
        return self.user.username


# class UserProject (models.Model):

#     """ User connected to set of projects. """

#     user = models.ForeignKey(User)
#     project = models.ForeignKey(Project)
