#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from django.conf.urls import patterns, url, include
from MilkShake.settings import PLUGINS_DIR

from Plugins import views

urlpatterns = patterns('',

    # Listage des plugins utilisateur
    url(r'^pluginsAndWidgets', views.get_plugins_and_widgets, name='get_plugins_and_widgets'),

    # Chargement d'une ressource de widget
    url(r'^widgetResource', views.get_widget_resource, name='get_widget_resource'),

)

# Recherche des routes des plugins
for plugin_folder in os.listdir(PLUGINS_DIR):
    # Filtrage uniquement des plugins possèdant un fichier de routage
    if os.path.isdir(PLUGINS_DIR + '/' + plugin_folder) and os.path.isfile(PLUGINS_DIR + '/' + plugin_folder + '/urls.py'):
        print plugin_folder
        # Inclusion du fichier de routes du plugin
        urlpatterns += patterns('', url(r'^', include('Plugins.' + plugin_folder + '.urls',
                                                      namespace="Plugins." + plugin_folder)))