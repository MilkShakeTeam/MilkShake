#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext
import json
from forms import LoginForm


def index(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        return login(request)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home")

    # Messages d'erreur
    error_missing_credentials = ugettext(u"Please fill all the fields.")
    error_bad_credentials     = ugettext(u"Incorrect login or password.")
    error_user_not_active     = ugettext(u"This user is currently inactive.")

    if request.POST and request.is_ajax():
        contact_form = LoginForm(request.POST)
        if contact_form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    # Authentification de l'utilisateur
                    django_login(request, user)

                    return HttpResponse(json.dumps({"success": True}))
                else:
                    return HttpResponseBadRequest(json.dumps({"success": False, "message": error_user_not_active}))
            else:
                return HttpResponseBadRequest(json.dumps({"success": False, "message": error_bad_credentials}))
        else:
            return HttpResponseBadRequest(json.dumps({"success": False, "message": error_missing_credentials}))
    else:
        contact_form = LoginForm()

    return render(request, 'login.html', {'form': contact_form})


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/login")


@login_required
def home(request):
    return render(request, 'home.html')