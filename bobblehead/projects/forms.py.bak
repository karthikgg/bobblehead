from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    tags_list = forms.CharField()
    articles = forms.CharField()
    # articles_list = forms.CharField()

    class Meta:
        model = Project
        exclude = ('user', 'tags', 'articles', 'category')


class ProjectUpdate(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
