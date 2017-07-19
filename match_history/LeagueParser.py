from urllib.request import urlopen
import json
import datetime

from .models import Account


class MatchHistoryParser:

    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = region
        self.match_history_json = None
        url_champions = 'https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=false&api_key=' + self.api_key
        champions = urlopen(url_champions)
        champions_string = champions.read().decode('utf-8')
        champions_json = json.loads(champions_string)
        champions_json = champions_json['data']
        self.champions = {}
        for key, val in champions_json.items():
            self.champions[str(val['id'])] = champions_json[key]

    def get_match_history(self, account_id):
        url = 'https://' + self.region + '.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(account_id) + '/recent?api_key=' + self.api_key
        match_history = urlopen(url)
        match_history_string = match_history.read().decode('utf-8')
        self.match_history_json = json.loads(match_history_string)

    def convert_match_data(self):
        self.match_history_json = self.match_history_json['matches']
        # update time from int to datetime
        for match in self.match_history_json:
            temp = match['timestamp'] / 1000.0
            match['timestamp'] = datetime.datetime.fromtimestamp(temp)
            match['championName'] = self.champions[str(match['champion'])]['name']
            match['championName'] = match['championName'].lower().title()
        return self.match_history_json

    def get_match_details(self, game_id):
        url = 'https://' + self.region + '.api.riotgames.com/lol/match/v3/matches/' + str(game_id) + '?api_key=' + self.api_key
        match = urlopen(url)
        match_string = match.read().decode('utf-8')
        return json.loads(match_string)


class AccountParser:

    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = region

    def get_account_by_summoner_name(self, summoner_name):
        url = 'https://' + self.region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summoner_name + '?api_key=' + self.api_key
        summoner = urlopen(url)
        summoner_string = summoner.read().decode('utf-8')
        summoner_json = json.loads(summoner_string)
        is_present = bool(Account.objects.filter(account_id=summoner_json['accountId']))
        if not is_present:
            Account.objects.create(
                account_id=summoner_json['accountId'],
                summoner_name=summoner_json['name'].lower(),
                profile_icon_id=summoner_json['profileIconId'],
                summoner_level=summoner_json['summonerLevel']
            )



