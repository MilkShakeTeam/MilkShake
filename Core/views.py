#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
from Core.decorators import ajax_required
from forms import LoginForm


def index(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        return render(request, 'login.html', {'form': LoginForm()})


@ajax_required
def login(request):
    contact_form = LoginForm(request.POST)
    errors = form_validate(contact_form)

    if not errors:
        django_login(request, authenticate(username=request.POST['username'], password=request.POST['password']))
        return HttpResponse(json.dumps({"success": True}))
    else:
        return HttpResponseBadRequest(errors)


def form_validate(form):
    """
    Validation d'un formulaire
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


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/")


@login_required
def home(request):
    return render(request, 'home.html')