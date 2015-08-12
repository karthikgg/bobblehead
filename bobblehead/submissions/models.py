from django.db import models
from webapp.models import Project
from user_profile.models import UserProfile


# Create your models here.
class Submission(models.Model):

    """ project submission details """
    # project object
    project = models.ForeignKey(Project)
    # URLField defaults to 200 max length, to hold submission link
    link = models.URLField()
    # user who added this submission
    # user = models.ForeignKey(UserProfile)
    members = models.ManyToManyField(UserProfile)

    description = models.TextField()

    def __unicode__(self):
        """ Return the tag name to better identify object. """
        return self.project.title


""" How to add members
from webapp.models import Project
from user_profile.models import UserProfile
from submissions.models import Submission

u_p = UserProfile.objects.get(email="pshevade@gmail.com")
pro = Project.objects.get(title="Bobblehead")
u_2 = UserProfile.objects.get(email="2nd.engineering.life@gmail.com")
u_3 = UserProfile.objects.get(email="test@test")

sub = Submission(project=pro, link='www.github.com', user=u_p, description="Test test test")

sub = Submission(project=pro, link='www.github.com',  description="test")
>>> sub.save()
>>> sub.members.add(u_p)
>>> sub.members.add(u_2)
>>> sub.members.add(u_2)
>>> sub.members.add(u_3)
>>> sub.save()
>>> sub.members
<django.db.models.fields.related.ManyRelatedManager object at 0xb68bc7ec>
>>> for m in sub.members: m.nickname
... 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'ManyRelatedManager' object is not iterable
>>> sub.members.all()
[<UserProfile: P-dawg>, <UserProfile: Test Account>, <UserProfile: Second Test Account>]
>>> sub.members.get(email='pshevade@gmail.com')
<UserProfile: P-dawg> """
