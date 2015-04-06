#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from Core.decorators import *

from Plugins.PyNchLine.common.pynchline import PyNchLine

# TODO - Mutualisation
# TODO - Commentaires
# TODO - Refaire pynchline pour découpler get_random_lyrics_by_artist et get_random_song_by_artist
# TODO - Ajouter des feats à pynchline !

@login_required_ajax
def get_lyrics_by_search_terms(request):
    # Validation de la recherche
    search = request.GET.get('search')
    if search is None:
        return HttpResponseBadRequest()

    # Récupération des lyrics
    lyrics = PyNchLine.get_lyrics_by_search_terms(search)

    # On retourne les informations associées
    return JsonResponse({
        "success": True,
        "data": {
            "lyrics": lyrics,
        }
    })

@login_required_ajax
def get_random_lyrics_by_artist(request):
    # Validation de l'artiste
    artist = request.GET.get('artist')
    if artist is None:
        return HttpResponseBadRequest()

    # Récupération de la punchline et de son morceau associé
    song = PyNchLine.get_random_lyrics_by_artist(artist, with_song_name=True)

    # On retourne les informations associées
    return JsonResponse({
        "success": True,
        "data": {
            "artist_name": artist,
            "song_name": song[0],
            "lyrics": song[1]
        }
    })

@login_required_ajax
def get_random_song_by_artist(request):
    # Validation de l'artiste
    artist = request.GET.get('artist')
    if artist is None:
        return HttpResponseBadRequest()

    # Récupération de la punchline et de son morceau associé
    song = PyNchLine.get_random_lyrics_by_artist(artist, with_song_name=True)

    # On retourne les informations associées
    return JsonResponse({
        "success": True,
        "data": {
            "artist_name": artist,
            "song_name": song[0],
        }
    })

@login_required_ajax
def get_random_punchline_by_artist(request):
    # Validation de l'artiste
    artist = request.GET.get('artist')
    if artist is None:
        return HttpResponseBadRequest()

    # Récupération de la punchline et de son morceau associé
    punchline = PyNchLine.get_random_punchline_by_artist(artist, with_song_name=True)

    # On retourne les informations associées
    return JsonResponse({
        "success": True,
        "data": {
            "artist_name": artist,
            "song_name": punchline[0],
            "punchline": punchline[1],
        }
    })