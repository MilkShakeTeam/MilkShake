#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from Core import views

urlpatterns = patterns('',
    # Route principale
    url(r'^$', views.index, name='index'),

    # Connexion
    url(r'^doLogin', views.do_login, name='do_login'),

    # Logout
    url(r'^logout', views.logout, name='logout'),
)