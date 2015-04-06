#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url, include

from Plugins import views

urlpatterns = patterns('',

    # Listage des plugins utilisateur
    url(r'^pluginsAndWidgets', views.get_plugins_and_widgets, name='get_plugins_and_widgets'),

    # TODO - Trouver comment mapper automatiquement les routes présentes dans PyNchLine ici
    url(r'^', include('Plugins.PyNchLine.urls', namespace="Plugins.PyNchLine")),

    # Ajout des sources des plugins, accessibles via /plugin/
    # Le fait de mettre cette route APRES les urls de PyNchLine fait qu'elles ont moins de priorité, et que ça marche

    # TODO - TOUT est accessible par ce biais, peut-être limiter sur un certain type de fichier ? (genre, js)
    #         Pourquoi ne pas faire passer la récupération des fichiers JS, HTML par un controlleur ? ça permettrait
    #         de gérer la validation des fichiers, et leurs traductions
    url(r'^plugin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PLUGINS_DIR}),
)