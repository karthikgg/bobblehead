""" urls.py for user_profile """
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login_projects/$', views.login_projects, name='login_projects'),
    url(r'login_udacity/$', views.login_udacity, name='login_udacity'),
    # url(r'^udacity_user/$', views.udacity_user, name='udacity_user'),
    url(r'^logout/$', views.logout_projects, name='logout_projects'),
    url(r'^show/(?P<user_key>[\w.-]+)/$', views.show, name='show'),
    url(r'^view/(?P<user_key>[\w.-]+)/$', views.view, name='view'),
    url(r'^edit/$', views.edit, name='edit'),
]
