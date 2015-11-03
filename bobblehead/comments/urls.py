from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'(?P<sub_id>[0-9]+)/new_comment/$', views.new_comment, name='new_comment'),
    url(r'^comments_JSON/(?P<sub_id>[0-9]+)$', views.comments_JSON, name='comments_JSON'),
]
