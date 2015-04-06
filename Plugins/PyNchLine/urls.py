#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from Plugins.PyNchLine import views

urlpatterns = patterns('',
    # Récupération des lyrics associés à une recherche
    url(r'^plugin/pynchline/getLyricsBySearchTerms', views.get_lyrics_by_search_terms, name='get_lyrics_by_search_terms'),

    # Récupération des lyrics d'une chanson aléatoire associés à un artiste
    url(r'^plugin/pynchline/getRandomLyricsByArtist', views.get_random_lyrics_by_artist, name='get_random_lyrics_by_artist'),

    # Récupération d'un titre de chanson aléatoire associé à un artiste
    url(r'^plugin/pynchline/getRandomSongByArtist', views.get_random_song_by_artist, name='get_random_song_by_artist'),

    # Récupération d'une random punchline associés à un artiste
    url(r'^plugin/pynchline/getRandomPunchlineByArtist', views.get_random_punchline_by_artist, name='get_random_punchline_by_artist'),
)