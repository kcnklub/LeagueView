from .LeagueAPI import LeagueAPI
from urllib.request import urlopen
from match_history.models import Match, Player
import json


class MatchTool(LeagueAPI):

    def __init__(self, api_key, region):
        LeagueAPI.__init__(self, api_key, region)

    def save_match(self, game_id, summoner_id = ''):

        # get the match information from riot and convert it to a json object.
        match_url = ''
        if not summoner_id == '':
            match_url = 'https://' + self.region + '.api.riotgames.com/lol/match/v3/matches/' + str(game_id) + '?forAccountId=' + str(summoner_id) +'&api_key=' + self.api_key
        else:
            match_url = 'https://' + self.region + '.api.riotgames.com/lol/match/v3/matches/' + str(game_id) + '?api_key=' + self.api_key

        match = urlopen(match_url)
        match_string = match.read().decode('utf')
        match_json = json.loads(match_string)
        blue_team = match_json['teams'][0]
        red_team = match_json['teams'][1]
        players = match_json['participants']
        player_ids = match_json['participantIdentities']
        print(blue_team)
        print(red_team)

        # Create the match to save
        match_to_save = Match()

        # General Match Information
        match_to_save.game_id = game_id
        match_to_save.mode = match_json['gameMode']

        # this all of the information I can derive information for both teams.
        match_to_save.blue_team_win = blue_team['win']
        match_to_save.blue_team_first_blood = blue_team['firstBlood']
        match_to_save.blue_team_first_tower = blue_team['firstTower']
        match_to_save.blue_team_first_inhib = blue_team['firstInhibitor']
        match_to_save.blue_team_first_baron = blue_team['firstBaron']
        match_to_save.blue_team_first_herald = blue_team['firstRiftHerald']

        # blue team details
        match_to_save.blue_team_id = blue_team['teamId']
        match_to_save.blue_team_baron_kills = blue_team['baronKills']
        match_to_save.blue_team_dragon_kills = blue_team['dragonKills']
        match_to_save.blue_team_tower_kills = blue_team['towerKills']
        match_to_save.blue_team_rift_herald = blue_team['riftHeraldKills']
        match_to_save.blue_team_ban1 = blue_team['bans'][0]['championId']
        match_to_save.blue_team_ban2 = blue_team['bans'][1]['championId']
        match_to_save.blue_team_ban3 = blue_team['bans'][2]['championId']
        match_to_save.blue_team_ban4 = blue_team['bans'][3]['championId']
        match_to_save.blue_team_ban5 = blue_team['bans'][4]['championId']

        # red team details
        match_to_save.red_team_id = red_team['teamId']
        match_to_save.red_team_baron_kills = red_team['baronKills']
        match_to_save.red_team_dragon_kills = red_team['dragonKills']
        match_to_save.red_team_tower_kills = red_team['towerKills']
        match_to_save.red_team_rift_herald = red_team['riftHeraldKills']
        match_to_save.red_team_ban1 = red_team['bans'][0]['championId']
        match_to_save.red_team_ban2 = red_team['bans'][1]['championId']
        match_to_save.red_team_ban3 = red_team['bans'][2]['championId']
        match_to_save.red_team_ban4 = red_team['bans'][3]['championId']
        match_to_save.red_team_ban5 = red_team['bans'][4]['championId']

        # get the player information
        for idx, player in enumerate(player_ids):
            temp_part = Player()
            print(player)
            if 'player' in player:
                temp_part.summoner_id = player['player']['accountId']

            temp_part.participant_id = player['participantId']
            temp_part.team_id = players[idx]['teamId']
            temp_part.game_id = game_id
            temp_part.champion_id = players[idx]['championId']
            temp_part.summoner1_id = players[idx]['spell1Id']
            temp_part.summoner2_id = players[idx]['spell2Id']

            # stats
            temp_part.item0 = players[idx]['stats']['item0']
            temp_part.item1 = players[idx]['stats']['item1']
            temp_part.item2 = players[idx]['stats']['item2']
            temp_part.item3 = players[idx]['stats']['item3']
            temp_part.item4 = players[idx]['stats']['item4']
            temp_part.item5 = players[idx]['stats']['item5']
            temp_part.item6 = players[idx]['stats']['item6']
            temp_part.kills = players[idx]['stats']['kills']
            temp_part.deaths = players[idx]['stats']['deaths']
            temp_part.assists = players[idx]['stats']['assists']
            temp_part.largest_killing_spree = players[idx]['stats']['largestKillingSpree']
            temp_part.largest_multi_kill = players[idx]['stats']['largestMultiKill']
            temp_part.double_kills = players[idx]['stats']['doubleKills']
            temp_part.triple_kills = players[idx]['stats']['tripleKills']
            temp_part.quadra_kills = players[idx]['stats']['quadraKills']
            temp_part.penta_kills = players[idx]['stats']['pentaKills']

            try:
                print("trying")
                player_in_database = Player.objects.get(game_id=game_id, participant_id=temp_part.participant_id)
                print(str(player_in_database))
            except (Player.DoesNotExist, KeyError):
                print('the player DNE')
                temp_part.save()
            else:
                print('the player did but we updated')
                player_in_database.
                #player_in_database.save()





        # save the match
        match_to_save.save()











































