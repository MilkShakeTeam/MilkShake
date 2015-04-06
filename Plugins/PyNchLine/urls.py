#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from Plugins.PyNchLine import views

urlpatterns = patterns('',
    # Route principale
    url(r'^plugin/pynchline/getRandomPunchlineByArtist', views.get_random_punchline_by_artist, name='get_random_punchline_by_artist'),
)