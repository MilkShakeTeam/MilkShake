#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from django.core.management.base import NoArgsCommand
from termcolor import colored

# Récupération du répertoire du projet
from MilkShake.settings import BASE_DIR as PROJECT_DIR


class Command(NoArgsCommand):
    help = u"Créé l'intégralité des messages du projet"

    def handle_noargs(self, **options):
        # On boucle sur chaque dossier présent dans le projet
        for folder in os.listdir(PROJECT_DIR):
            # Est-ce que ce répertoire possède un dossier de locale ?
            if os.path.exists(os.path.join(PROJECT_DIR, folder, "locale")):
                # On suppose donc que ce répertoire est un dossier de projet; on se place dans le répertoire
                os.chdir(os.path.join(PROJECT_DIR, folder))

                # Génération des fichiers de traduction associés à l'application
                print colored("[" + folder + "]", 'red', attrs=['bold'])
                os.system("python django-admin.py makemessages -l fr --settings=settings")
                os.system("python django-admin.py makemessages -l pt --settings=settings")