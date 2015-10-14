from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    """ User Profile Form. """

    class Meta:
        model = UserProfile
        # don't want to change the email or the udacity key
        exclude = ('email', 'udacity_key',)
