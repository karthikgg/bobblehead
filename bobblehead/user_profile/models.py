""" user_profiles - to display user's information """
from django.db import models


# class UserProfileManager(models.Manager):
#     def get_by_natural_key(self, email, nickname):
#         return self.get(email=email, nickname=nickname)


# Create your models here.
class UserProfile(models.Model):
    # objects = UserProfileManager()

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
                                  choices=NANODEGREE_CHOICES, default='Developer')

    def __unicode__(self):
        """ Return the username to better identify object. """
        return self.nickname

    def natural_key(self):
        return (self.email, self.nickname)

    class Meta:
        unique_together = (('email', 'nickname'))
