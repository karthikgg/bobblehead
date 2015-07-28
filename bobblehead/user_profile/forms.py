from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    """ User Form. """

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'email', 'first_name', 'last_name')

    def save(self, commit=True):
        """ Overwrite the save method, to save email and password. """
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):

    """ User Profile Form. """

    class Meta:
        model = UserProfile
        fields = ('nanodegree',)
