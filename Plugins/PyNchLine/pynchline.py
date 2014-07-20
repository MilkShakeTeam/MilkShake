#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import random
import urllib2


class PyNchLine():
    """
    API de dialogue avec Rapgenius
    """

    # URL de base de Rapgenius
    base_url = "http://rapgenius.com/"

    # Copie des dernières données récupérées par pyNchLine
    last_call_data = ""

    # Constante d'url de recherche
    SEARCH_URL = "search?q="

    # Constante d'url des artistes
    ARTISTS_URL = "artists/"

    def __init__(self, base_url):
        """
        Constructeur

        :param base_url: Override de la base_url
        :type base_url: str
        """
        if base_url:
            self.base_url = base_url

    @classmethod
    def get_lyrics_by_search_terms(cls, search_terms):
        """
        Récupère les lyrics de la première chanson identifiée par les termes de recherche passés en paramètre

        :param search_terms: Termes de recherche
        :type search_terms: str
        :returns List
        """

        # Récupération du contenu brut de la page
        html = cls.__call_rapgenius(ctx="search", param=search_terms.replace(" ", "+"))

        # Récupération de l'url la plus proche
        song_url = html.find("a", " song_link")['href']

        # On retourne les lyrics liées à cette url
        return cls.get_lyrics_by_url(song_url)

    @classmethod
    def get_lyrics_by_url(cls, url):
        """
        Récupère les lyrics du lien Rapgenius passé en paramètre

        :param url: Lien rapgenius
        :type url: str
        :returns List
        """

        # Récupération du contenu brut de la page
        html = cls.__call_rapgenius(url=url)

        # On itère sur chaque chaine (strippée) de la première div.lyrics
        # Chaque ligne de lyric est placée dans une entrée séparée du tableau
        # pour faciliter les manipulations ultérieures
        lyrics = []
        for string in html.find("div", "lyrics").stripped_strings:
            lyrics.append(string)

        return lyrics

    @classmethod
    def get_random_song_by_artist(cls, artist, with_song_name=False):
        """
        Récupère une random chanson de l'artiste passé en paramètre

        :param artist: Artiste
        :type artist: str
        :returns List
        """

        # Récupération du contenu brut de la page
        html = cls.__call_rapgenius(ctx="artists", param=artist.replace(" ", "-"))

        # Récupération des différentes chansons de l'artiste
        all_songs = html.find("section", "all_songs").find_all("a", "song_name")

        # Récupération d'un lien au hasard
        song_url = random.choice(all_songs)['href']

        # Récupération des lyrics
        song_lyrics = cls.get_lyrics_by_url(cls.base_url + song_url)

        if not with_song_name:
            # On retourne directement les lyrics par défaut
            return song_lyrics
        else:
            # Si demandé; on retourne le nom de la piste en plus
            return [cls.last_data.find("span", "text_title").string, song_lyrics]

    @classmethod
    def get_random_punchline_by_artist(cls, artist, with_song_name=False):
        """
        Récupère une random puchline de l'artiste passé en paramètre

        :param artist: Artiste
        :type artist: str
        :returns str
        """

        # Récupération des lyrics d'une chanson au hasard de l'artiste
        song_lyrics = cls.get_random_song_by_artist(artist)

        # On retourne une punchline au hasard, ni vide, [ni comme ceci]
        punchline = ""
        while ("[" in punchline and "]" in punchline) or (punchline == ""):
            punchline = random.choice(song_lyrics)

        if not with_song_name:
            # On retourne directement la punchline par défaut
            return punchline
        else:
            # Si demandé; on retourne le nom de la piste en plus
            return [cls.last_data.find("span", "text_title").string, punchline]

    @classmethod
    def __call_rapgenius(cls, ctx=None, param=None, url=None):
        """
        Lance une requête de récupération de contenu vers rapgenius

        :param ctx: Contexte (search|artists)
        :type ctx: str
        :param param: Paramètres au format GET supplémentaires
        :type param: str
        :param url: Url d'appel vers rapgenius
        :type param: str
        :returns List
        """

        if not url:
            # Si pas d'url passée en paramètre; formattage de l'url en fonction du contexte
            url = cls.base_url + (cls.SEARCH_URL if ctx == "search" else
                                 (cls.ARTISTS_URL if ctx == "artists" else None)) + param
        else:
            # Si une url est passée en paramètre (appel explicite), exception si celle-ci ne pointe pas vers Rapgenius
            if not cls.base_url in url:
                raise Exception("Not a valid Rapgenius URL.")

        # On retourne le contenu soupé (sauvegardé en cache si besoin ultérieur éventuel)
        html = urllib2.urlopen(url).read()
        cls.last_data = BeautifulSoup(html)
        return cls.last_data