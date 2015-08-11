from django.conf.urls import url
# from webapp.views import project_create, project_delete, project_update
from . import views
from . import models
from django.contrib.auth import views as auth_views


# jeff = models.Tag()
# jeff.tag_name = "jeff"

# karthik = models.Tag()
# karthik.tag_name = "karthik"
# the_tags = [jeff, karthik]

# print "These are the tags: ", the_tags

urlpatterns = [
    # ex: /projects/
    url(r'^$', views.index, name='index'),
    # ex: /projects/5/
    url(r'^(?P<project_id>[0-9]+)/$', views.project_detail, name='detail'),
    url(r'^(?P<project_id>[0-9]+)/edit_project', views.edit_project, name='edit_project'),
    url(r'request_meta/$', views.request_meta, name='request_meta'),
    url(r'create_project/$', views.create_project, name='create_project'),
    url(r'^(?P<project_id>[0-9]+)/delete_project', views.delete_project, name='delete_project'),
    url(r'^projects_JSON/$', views.projects_JSON, name='projects_JSON'),
    url(r'^query_projects/$', views.query_projects, name='query_projects'),
    # ex: /projects/createproject
    #url(r'createproject/$',
    #    views.project_create, name='createproject'),
    # ex: /projects/5/updateproject
    # url(r'^(?P<project_id>[0-9]+)/update/$',
    #     views.update_project, name='update'),
    # url(r'createproject/$', project_create.as_view(), name='createproject'),
    # url(r'project/(?P<pk>[0-9]+)/$', project_update.as_view(), name='updateproject'),
    # url(r'project/(?P<pk>[0-9]+)/delete/$', project_delete.as_view(), name='deleteproject'),
    # #url(r'thanks/$', views.index, name='thanks'),
    # ex: /projects/5/deleteproject
    #url(r'^(?P<question_id>[0-9]+)/dele/$', views.vote, name='vote'),
]
