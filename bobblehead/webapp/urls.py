from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.project_detail, name='detail'),
    url(r'^(?P<project_id>[0-9]+)/edit_project', views.edit_project, name='edit_project'),
    url(r'request_meta/$', views.request_meta, name='request_meta'),
    url(r'create_project/$', views.create_project, name='create_project'),
    url(r'^(?P<project_id>[0-9]+)/delete_project', views.delete_project, name='delete_project'),
    url(r'^projects_JSON/$', views.projects_JSON, name='projects_JSON'),
    url(r'^tags_JSON/$', views.tags_JSON, name='tags_JSON'),
    url(r'^query_projects/$', views.query_projects, name='query_projects'),
]
