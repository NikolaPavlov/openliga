import requests


class OpenLigaSDK:
    def __init__(self):
        self.URL = 'https://www.openligadb.de/api/'

        self.league = 'bl1'
        self.season = '2020'

    def get_all_games(self):
        response = requests.get(self.URL + 'getmatchdata' + '/' + self.league + '/' + self.season)
        return response.json()

    def get_all_teams(self):
        response = requests.get('https://www.openligadb.de/api/' + 'getavailableteams' + '/' + self.league + '/' + self.season)
        print(response.json())
        return response.json()
