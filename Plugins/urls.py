#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from django.conf import settings
from django.conf.urls import patterns, url, include
from MilkShake.settings import PLUGINS_DIR

from Plugins import views

urlpatterns = patterns('',

    # Listage des plugins utilisateur
    url(r'^pluginsAndWidgets', views.get_plugins_and_widgets, name='get_plugins_and_widgets'),

)

# Recherche des routes des plugins
for plugin_folder in os.listdir(PLUGINS_DIR):
    # Filtrage uniquement des plugins possèdant un fichier de routage
    if os.path.isdir(PLUGINS_DIR + '/' + plugin_folder) and os.path.isfile(PLUGINS_DIR + '/' + plugin_folder + '/urls.py'):
        print plugin_folder
        # Inclusion du fichier de routes du plugin
        urlpatterns += patterns('', url(r'^', include('Plugins.' + plugin_folder + '.urls',
                                                      namespace="Plugins." + plugin_folder)))

# TODO - TOUT est accessible par ce biais, peut-être limiter sur un certain type de fichier ? (genre, js)
#        Pourquoi ne pas faire passer la récupération des fichiers JS, HTML par un controlleur ? ça permettrait
#        de gérer la validation des fichiers, et leurs traductions associées
urlpatterns += patterns('', url(r'^plugin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PLUGINS_DIR}))