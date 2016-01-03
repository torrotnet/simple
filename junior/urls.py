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
    url(r'^success-story/$', 'success_story.views.success_story_list', name='success_story_list'),
    url(r'^success-story/(?P<id>[0-9]+)/$', 'success_story.views.success_story', name='success_story'),
    url(r'^success-story/new/$', 'success_story.views.success_story_new', name='success_story_new'),
    url(r'^success-story/new/thank_you$', 'success_story.views.success_story_new_thank_you', name='success_story_new_thank_you'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'success_story.views.home', name='home'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^should-know/$', 'should_know.views.should_know_list', name='should_know_list'),
    url(r'^should-know/person/(?P<id>[0-9]+)/$', 'should_know.views.should_know_person', name='should_know_person'),
    url(r'^should-know/company/(?P<id>[0-9]+)/$', 'should_know.views.should_know_company', name='should_know_company'),
    url(r'^should_know/person/new/$', 'should_know.views.should_know_person_new', name='should_know_person_new'),
    # url(r'^should_know/company/new/$', 'should_know.views.should_know_company_new', name='should_know_company_new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
