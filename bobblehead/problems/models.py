from django.db import models

from projects.models import Tag
from user_profile.models import UserProfile
from comments.models import Question, Comment
# Create your models here.

CATEGORY_CHOICES = [('INTERVIEW', 'Interview Problem'),
                    ('CHALLENGE', 'Challenge Problem'),
                    ('QUESTION', 'The "I-have-a" Problem'),
                    ('CONTEST', 'Contest')]

DIFFICULTY_LEVEL = [('EASY', 'Easy'),
                    ('MEDIUM', 'Medium'),
                    ('HARD', 'Hard')]



class Problem(models.Model):

    """ Problem model to hold the information about a problem. """
    user = models.ForeignKey(UserProfile, default=None)
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted = models.DateField(auto_now_add=True)

    category = models.CharField(max_length=15,
                                choices=CATEGORY_CHOICES,
                                default='CHALLENGE')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVEL, default=1)
    # due_date = models.DateTimeField(default=None)
    tags = models.ManyToManyField(Tag)
    questions = models.ManyToManyField(Question)


class Solution(models.Model):

    user = models.ForeignKey(UserProfile, default=None)
    title = models.CharField(max_length=200, default=None)
    problem = models.ForeignKey(Problem, default=None)
    description = models.TextField()
    posted = models.DateField(auto_now_add=True)
    comments = models.ManyToManyField(Comment)
