#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from Core import views


urlpatterns = patterns('',
    # Route principale
    url(r'^$', views.index, name='index'),

    # Route ajax
    url(r'^login', views.login, name='ajax_login'),

    # A revamper
    url(r'^logout', views.logout, name='logout'),
)