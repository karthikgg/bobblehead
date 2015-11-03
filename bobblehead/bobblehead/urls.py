"""
Bobblehead URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from projects import views as projects_views

urlpatterns = [
    url(r'^$', projects_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^user_profile/', include('user_profile.urls', namespace="user_profile")),
    url(r'^submissions/', include('submissions.urls', namespace="submissions")),
    url(r'^comments/', include('comments.urls', namespace="comments"))
]
