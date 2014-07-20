#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from Core import views


urlpatterns = patterns('',
    # Route principale
    url(r'^$', views.index, name='index'),

    # Connexion
    url(r'^doLogin', views.do_login, name='do_login'),

    # Listage des plugins utilisateur
    url(r'^listUserPlugins', views.list_user_plugins, name='list_user_plugins'),

    # Logout
    url(r'^logout', views.logout, name='logout'),
)