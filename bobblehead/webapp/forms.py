from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    tags_list = forms.CharField()

    class Meta:
        model = Project
        # fields = ['title', 'desrciption', 'collaborators', 'posted',
        #           'category', 'articles', 'tags']
        exclude = ('user', 'tags')


class ProjectUpdate(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
