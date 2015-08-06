""" urls.py for user_profile """
from django.conf.urls import url

from . import views
from . import models

urlpatterns = [
    url(r'login_webapp/$', views.login_webapp, name='login_webapp'),
    url(r'login_udacity/$', views.login_udacity, name='login_udacity'),
    url(r'^create_profile/$', views.create_profile, name='create_profile'),
    url(r'^udacity_user/$', views.udacity_user, name='udacity_user'),
    url(r'^logout/$', views.logout_webapp, name='logout_webapp'),
    url(r'^show_profile/$', views.show_profile, name='show_profile'),
]
