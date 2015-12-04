"""hue_nlp URL Configuration

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
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home'),
    url(r'^signup', 'main.views.sign_up'),
    url(r'^signin', 'main.views.sign_in'),
    url(r'^profile', 'Interface.views.profile'),
    url(r'^social', 'Interface.views.social'),
    url(r'^preferences', 'Interface.views.preferences'),
    url(r'^hue', 'Interface.views.hue'),
    url(r'^account', 'Interface.views.account'),
    #remember to remove before deploying
    url(r'^500/$', 'main.views.handler500'),
    url(r'^404/$', 'main.views.handler404'),
]
