#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.forms.util import ErrorList
from django.forms.forms import NON_FIELD_ERRORS


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=5)
    password = forms.CharField(required=True, max_length=5)

    def clean(self):
        """
        Validation sur plusieurs champs (ici, gestion du couple login/mot de passe)
        https://docs.djangoproject.com/en/dev/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
        """

        cleaned_data = super(LoginForm, self).clean()

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
                errors.append(u"Incorrect login or password")
            # Si l'utilisateur est inactif
            else:
                if not user.is_active:
                    errors = self._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
                    errors.append(u"User is inactive")

        return cleaned_data