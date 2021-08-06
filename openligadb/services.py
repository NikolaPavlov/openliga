import requests

from django.conf import settings


class OpenLigaSDK:
    def __init__(self):
        pass

    def get_all_games(self):
        response = requests.get(settings.API_URL + '/' + 'getmatchdata' + '/' + settings.LEAGUE + '/' + settings.SEASON)
        return response.json()

    def get_all_teams(self):
        response = requests.get(settings.API_URL + '/' + 'getavailableteams' + '/' + settings.LEAGUE + '/' + settings.SEASON)
        return response.json()

    def get_all_stats(self):
        response = requests.get(settings.API_URL + '/' + 'getbltable' + '/' + settings.LEAGUE + '/' + settings.SEASON)
        return response.json()
