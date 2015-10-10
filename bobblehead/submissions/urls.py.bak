# urls for submission

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new/(?P<project_id>[0-9]+)/$', views.new_submission, name='new_submission'),
    url(r'^show/(?P<submission_id>[0-9]+)/$', views.show_submission, name='show_submission'),
]
