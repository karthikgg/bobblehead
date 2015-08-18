""" user_profiles - to display user's information """
from django.db import models


# Create your models here.
class UserProfile(models.Model):

    """ User information. """
    email = models.CharField(max_length=100, default="")
    nickname = models.CharField(max_length=50, default="")
    udacity_key = models.CharField(max_length=10, default="")
    NANODEGREE_CHOICES = (('FULLSTACK', 'FullStack Developer'),
                          ('FRONTEND', 'Frontend Developer'),
                          ('ANDROID', 'Android Developer'),
                          ('DATA ANALYST', 'Data Analyst'),
                          ('IOS DEVELOPER', 'IOS Developer'))
    nanodegree = models.CharField(max_length=15,
                                  choices=NANODEGREE_CHOICES,)

    def __unicode__(self):
        """ Return the username to better identify object. """
        return self.nickname
