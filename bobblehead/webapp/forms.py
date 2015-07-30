from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = ['title', 'desrciption', 'collaborators', 'posted',
        #           'category', 'articles', 'tags']
        exclude = ('user',)


class ProjectUpdate(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
