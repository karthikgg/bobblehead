# urls for submission

from django.conf.urls import url
# from webapp.views import project_create, project_delete, project_update
from . import views
from . import models

urlpatterns = [
    # ex: /projects/
    url(r'^new/(?P<project_id>[0-9]+)/$', views.new_submission, name='new_submission'),
    # ex: /projects/5/
    # url(r'^edit/(?P<project_id>[0-9]+)/$', views.edit_submission, name='edit_submission'),
]
