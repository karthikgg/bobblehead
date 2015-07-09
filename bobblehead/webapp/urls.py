from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /projects/
    url(r'^$', views.index, name='index'),
    # ex: /projects/5/
    url(r'^(?P<project_id>[0-9]+)/$', views.project_detail, name='detail'),
    # ex: /projects/createproject
    url(r'createproject/$',
        views.create_project, name='createproject'),
    # ex: /projects/5/updateproject
    url(r'^(?P<project_id>[0-9]+)/update/$',
        views.update_project, name='update'),
    # ex: /projects/5/deleteproject
    #url(r'^(?P<question_id>[0-9]+)/dele/$', views.vote, name='vote'),
]
