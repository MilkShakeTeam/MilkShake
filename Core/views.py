#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import LoginForm
from Core.decorators import *
from Core.formutils import FormUtils

import json

def index(request):
    """
    Page principale de l'application.
    Rends la page de login si l'utilisateur n'es pas connecté, ou la page d'accueil dans le cas contraire.

    @TODO Gérer le rechargement du dernier composant utilisé si un F5 arrive (ou un bookmark ou whatever)
          Vraisemblablement a base de route + window.history.pushState

    :param request: Objet correspondant a la requête utilisateur
    :type request: HttpRequest
    :return: La vue et son code HTTP correspondant
    :rtype: HttpResponse
    """

    # Vérification de l'état d'auth de l'utilisateur afin de rendre la vue/action souhaitée
    if request.user.is_authenticated():
        return home(request)
    else:
        return login(request)


def login(request):
    """
    Rends la page de login.

    :param request: Objet correspondant a la requête utilisateur.
    :type request: HttpRequest
    :return: La vue et son code HTTP correspondant
    :rtype: HttpResponse
    """

    return render(request, 'login.html', {'form': LoginForm()})


@ajax_required
def do_login(request):
    """
    Effectue une tentative de connexion de l'utilisateur.

    :param request: Objet correspondant a la requête utilisateur
    :type request: HttpRequest
    :return: Code HTTP et réponse au format json correspondant au succès (ou a l'échec) de la tentative de login
    :rtype: HttpResponse|HttpResponseBadRequest
    """

    # Récupération du contenu et validattion du formulaire
    contact_form = LoginForm(request.POST)
    errors = FormUtils.validate(contact_form)

    if not errors:
        # Pas d'erreurs; on effectue le login utilisateur et on rends un objet json de succès
        django_login(request, authenticate(username=request.POST['username'], password=request.POST['password']))
        return HttpResponse(json.dumps({'success': True}))
    else:
        # Des erreurs sont survenues; on rends un code d'erreur avec les informations inhérentes en json
        return HttpResponseBadRequest(errors)


@login_required
def logout(request):
    """
    Rends la page de logout.

    :param request: Objet correspondant a la requête utilisateur.
    :type request: HttpRequest
    :return: La vue et son code HTTP correspondant
    :rtype: HttpResponse
    """

    # Déconnexion de l'utilisateur et redirection vers la page de login
    django_logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    """
    Rends la page d'accueil.

    :param request: Objet correspondant a la requête utilisateur
    :type request: HttpRequest
    :return: La vue et son code HTTP correspondant
    :rtype: HttpResponse
    """

    # Affichage de la page d'accueil
    return render(request, 'home.html')