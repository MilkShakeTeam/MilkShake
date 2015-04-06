#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from Core.decorators import *

from Plugins.PyNchLine.common.pynchline import PyNchLine

@login_required_ajax
def get_random_punchline_by_artist(request):
    # Validation de l'artiste
    artist = request.GET.get('artist')
    if artist is None:
        return HttpResponseBadRequest()

    # Récupération de la punchline et de son morceau associé
    punchline = PyNchLine.get_random_punchline_by_artist("kaaris", with_song_name=True)

    # On retourne les informations associées
    return JsonResponse({
        "success": True,
        "data": {
            "artist_name": artist,
            "song_name": punchline[0],
            "punchline": punchline[1],
        }
    })