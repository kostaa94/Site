"""shop URL Configuration

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
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings

urlpatterns = i18n_patterns('',

    url(r'^product/', include('store.urls')),
    url(r'^$', include('store.urls')),
    url(r'^shop/', include('store.urls')),
    url(r'^checkout/',include('store.urls')),
    url(r'^cart/',include('store.urls')),
    url(r'^login/',include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),
)



##urlpatterns = [
##    url(r'^shop/',include('store.urls')),
##    url(r'^product/',include('store.urls')),
###    url(r'^checkout/',include('store.urls')),
##    url(r'^$',include('store.urls')),
##    url(r'^admin/', include(admin.site.urls)),
##
##]
