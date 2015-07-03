from django.db import models

# Create your models here.
class Tag(models.Model):
    """ Description for tags goes here """
    #tags = models.ForeignKey(Project)
    tag_name = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.tag_name

class Project(models.Model):
    """ Description for models goes here """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length = 5000)
    collaborators = models.IntegerField(default=1)
    posted = models.DateField(db_index=True, auto_now_add=True)

    CATEGORY_CHOICES = (
        ('STUDENT', 'Student Project'),
        ('UDACITY', 'Udacity Project'),
        ('ENTERPRISE', 'Enterprise Project'),
        ('OPEN SOURCE', 'Open Source'),
        ('CONTEST', 'Contest'),
    )
    category = models.CharField(max_length=15,
                                      choices=CATEGORY_CHOICES,
                                      default='STUDENT')

    articles = models.CharField(max_length = 5000)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title


class User(models.Model):
    """ Description goes here """
    
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    NANODEGREE_CHOICES = (
        ('FULLSTACK', 'FullStack Developer'),
        ('FRONTEND', 'Frontend Developer'),
        ('ANDROID', 'Android Developer'),
        ('DATA ANALYST', 'Data Analyst'),
        ('IOS DEVELOPER', 'IOS Developer'),
    )
    nanodegree = models.CharField(max_length=15,
                                  choices=NANODEGREE_CHOICES,
                                      )

    def __unicode__(self):              # __unicode__ on Python 2
        return self.username

class UserProject (models.Model):
    """ User connected to set of projects """
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)


class TagsProject (models.Model):
    """ Tags connected to set of project """
    tag = models.ForeignKey(Tag)
    project = models.ForeignKey(Project)
