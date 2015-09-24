"""junior URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^success_story/$', 'success_story.views.success_story_list', name='success_story_list'),
    url(r'^success_story/(?P<id>[0-9])/$', 'success_story.views.success_story', name='success_story'),
    url(r'^success_story/new/$', 'success_story.views.success_story_new', name='success_story_new'),
    url(r'^success_story/new/thank_you$', 'success_story.views.success_story_new_thank_you', name='success_story_new_thank_you'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'success_story.views.home', name='home'),
    url(r'^summernote/', include('django_summernote.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
