# submission_forms
from django.forms import ModelForm
from .models import Submission


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        exclude = ('project', 'members')
