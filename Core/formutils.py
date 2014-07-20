#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


class FormUtils():
    """
    Classe de gestion utilitaire des formulaires de l'application.
    """

    @classmethod
    def validate(cls, form):
        """
        Permet de procéder a la validation d'un formulaire.

        :param form: Formulaire à valider
        :type form: Form
        :return: Chaîne au format JSON si des erreurs sont survenues, None sinon
        :rtype: String|None
        """

        # Récupération des erreurs du formulaire si celui-ci est invalide
        errors = {}
        if not form.is_valid():
            # Validation de chaque champ
            for field in form:
                if field.errors:
                    errors[field.html_name] = []
                    for error in field.errors:
                        errors[field.html_name].append(error)

            # Ajout des erreurs non-liées directement à des champs si existantes
            non_field_errors = form.non_field_errors()
            if non_field_errors:
                errors["NON_FIELD_ERRORS"] = []
                for error in non_field_errors:
                    errors["NON_FIELD_ERRORS"].append(error)

        # On retourne les erreurs au format json ou null si pas d'erreurs
        return json.dumps({"errors": errors}) if errors else None