from django.conf.urls import url
from webapp.views import project_create, project_delete, project_update
from . import views
from . import models


jeff = models.Tag()
jeff.tag_name = "jeff"

karthik = models.Tag()
karthik.tag_name = "karthik"
the_tags = [jeff, karthik]

print "These are the tags: ", the_tags

urlpatterns = [
    # ex: /projects/
    url(r'^$', views.index, name='index'),
    # ex: /projects/5/
    url(r'^(?P<project_id>[0-9]+)/$', views.project_detail, name='detail'),
    # ex: /projects/createproject
    #url(r'createproject/$',
    #    views.project_create, name='createproject'),
    # ex: /projects/5/updateproject
    url(r'^(?P<project_id>[0-9]+)/update/$',
        views.update_project, name='update'),
    url(r'createproject/$', project_create.as_view(), name='createproject'),
    url(r'project/(?P<pk>[0-9]+)/$', project_update.as_view(), name='updateproject'),
    url(r'project/(?P<pk>[0-9]+)/delete/$', project_delete.as_view(), name='deleteproject'),
    # ex: /projects/5/deleteproject
    #url(r'^(?P<question_id>[0-9]+)/dele/$', views.vote, name='vote'),
]