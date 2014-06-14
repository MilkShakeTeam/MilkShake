#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.forms.util import ErrorList
from django.forms.forms import NON_FIELD_ERRORS
from django.utils.translation import ugettext as _


class LoginForm(forms.Form):
    """
    Formulaire de connexion à l'application
    """

    # Placeholder du nom de l'utilisateur
    PLACEHOLDER_USERNAME = _("Enter your username")
    # Placeholder du mot de passe
    PLACEHOLDER_PASSWORD = _("Enter your password")

    # Erreur; mauvais couple login/mot de passe
    ERROR_WRONG_CRED = _("Incorrect login or password")
    # Erreur; utilisateur inactif
    ERROR_USER_INACTIVE = _("Incorrect login or password")

    # Champ utilisateur
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'username',
            'class': 'form-control input-sm center',
            'placeholder': PLACEHOLDER_USERNAME,
            'required': 'required'
        })
    )

    # Champ mot de passe
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'class': 'form-control input-sm center',
            'placeholder': PLACEHOLDER_PASSWORD,
            'required': 'required'
        })
    )

    def clean(self):
        """
        Validation sur plusieurs champs (ici, gestion du couple login/mot de passe)
        https://docs.djangoproject.com/en/dev/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
        """

        # Appel de la validation parente
        cleaned_data = super(LoginForm, self).clean()

        # Récupération de l'état de validation des champs du formulaire
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Validation sur le couple, uniquement si ces champs sont déjà valides
        if username and password:
            # Tentative de récupération de l'utilisateur
            user = authenticate(username=username, password=password)

            # Si l'utilisateur n'a pas été trouvé
            if user is None:
                # http://stackoverflow.com/questions/188886/inject-errors-into-already-validated-form
                errors = self._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
                errors.append(self.ERROR_WRONG_CRED)
            # Si l'utilisateur est inactif
            else:
                if not user.is_active:
                    errors = self._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
                    errors.append(self.ERROR_USER_INACTIVE)

        return cleaned_data