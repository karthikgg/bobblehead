""" urls.py for user_profile """
from django.conf.urls import url

from . import views
from . import models

urlpatterns = [
    url(r'^create_profile/$', views.create_profile, name='create_profile')
]
