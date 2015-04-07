#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import JsonResponse, HttpResponseNotFound
from Core.decorators import *
from MilkShake.settings import PLUGINS_DIR

import mimetypes
import json
import os

@login_required_ajax
def get_plugins_and_widgets(request):
    """
    Retourne au format JSON l'intégralité des plugins et widgets de l'application

    :param request: Objet correspondant a la requête utilisateur
    :type request: HttpRequest
    :return: Code HTTP et réponse au format json correspondant aux plugins disponibles pour l'utilisateur
    :rtype: JsonResponse
    """

    plugin_list = {"widgets": {}, "plugins": {}}

    # Récupération des plugins et widgets de l'application
    for plugin_folder in os.listdir(PLUGINS_DIR):
        base_path = PLUGINS_DIR + '/' + plugin_folder

        # Validation de la présence du dossier de widgets
        if os.path.exists(base_path + '/widget/'):

            # Récupération des widgets du plugin
            for widget_folder in os.listdir(base_path + '/widget/'):

                # Validation que l'élément soit bien un dossier, et que son code soit bien défini
                if os.path.isdir(os.path.join(base_path + '/widget/', widget_folder)) \
                        and os.path.isfile(os.path.join(base_path + '/widget/', widget_folder, 'widget.js')) \
                        and os.path.isfile(os.path.join(base_path + '/widget/', widget_folder, 'widget.json')):

                    # Tentative de récupération des données json associées au widget
                    try:
                        with open(os.path.join(base_path + '/widget/', widget_folder, 'widget.json')) as widget_json:
                            widget_properties = json.load(widget_json)
                    except ValueError:
                        # JSON inconnu ou incorrect ; on passe simplement au prochain widget
                        continue

                    # Ajout du widget si non existant
                    if not plugin_folder in plugin_list['widgets']:
                        plugin_list['widgets'][plugin_folder] = []

                    # Ajout des données du widget
                    plugin_list['widgets'][plugin_folder].append({
                        "name": widget_properties['name'] if 'name' in widget_properties else '',
                        "class": widget_properties['class'] if 'class' in widget_properties else '',
                        "resources": {
                            "js": "/widgetResource?plugin=" + plugin_folder + "&widget=" + widget_folder + "&resource_type=js",
                            "html": "/widgetResource?plugin=" + plugin_folder + "&widget=" + widget_folder + "&resource_type=html",
                        }
                    })

        # Validation du plugin
        if os.path.exists(base_path + '/plugin/'):
            # TODO - Que mettre ici ?
            # Proposition dans un premier temps : structure "nom_du_plugin": "route_du_plugin"
            # Mais comment configurer les routes à la volée ?
            plugin_list['plugins'][plugin_folder] = '/plugin/' + plugin_folder

    # On retourne la liste a l'utilisateur
    return JsonResponse(plugin_list)

@login_required_ajax
def get_widget_resource(request):
    # Récupération des paramètres d'entrée
    plugin = request.GET.get('plugin')
    widget = request.GET.get('widget')
    resource_type = request.GET.get('resource_type')

    # Validation basique des paramètres d'entrée
    if plugin is None or widget is None or resource_type is None or resource_type not in ['html', 'js']:
        return HttpResponseBadRequest()

    # Construction du chemin du fichier
    file_path = PLUGINS_DIR + '/' + plugin + '/widget/' + widget + '/widget.' + resource_type

    # Vérification de la présence du fichier
    if os.path.isfile(file_path):
        # Fichier présent ; on l'ouvre et retourne
        fsock = open(file_path, "r")
        return HttpResponse(fsock, mimetypes.guess_type(file_path))
    else:
        print PLUGINS_DIR + '/' + plugin + '/widget/' + widget + '/widget.' + resource_type
        return HttpResponseNotFound()