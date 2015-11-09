# urls for submission

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new/(?P<project_id>[0-9]+)/$', views.new_submission, name='new_submission'),
    url(r'^show/(?P<submission_id>[0-9]+)/$', views.show_submission, name='show_submission'),
    url(r'^(?P<submission_id>[0-9]+)/add_new_comment/', views.add_new_comment, name='add_new_comment'),
    url(r'(?P<sub_id>[0-9]+)/edit_comment/(?P<comment_id>[0-9]+)$', views.edit_comment, name='edit_comment'),
    url(r'(?P<sub_id>[0-9]+)/delete_comment/(?P<comment_id>[0-9]+)$', views.delete_comment, name='delete_comment'),
    
]
