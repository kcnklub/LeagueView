from django.db import models


class Account(models.Model):
    account_id = models.IntegerField()
    summoner_name = models.CharField(max_length=250)
    profile_icon_id = models.IntegerField()
    summoner_level = models.IntegerField()

    def __str__(self):
        return self.summoner_name + " - " + str(self.account_id)

    def get_account_id(self):
        return self.account_id



class Match(models.Model):
    game_id = models.IntegerField()
    ranked = models.BooleanField()

    # can determine red teams also
    blue_team_win = models.CharField(max_length=10)
    blue_team_first_blood = models.BooleanField()
    blue_team_first_tower = models.BooleanField()
    blue_team_first_inhib = models.BooleanField()
    blue_team_first_baron = models.BooleanField()
    blue_team_first_herald = models.BooleanField()

    # blue team details
    blue_team_id = models.IntegerField()
    blue_team_baron_kills = models.IntegerField()
    blue_team_dragon_kills = models.IntegerField()
    blue_team_tower_kills = models.IntegerField()
    blue_team_rift_herald = models.IntegerField()
    blue_team_ban1 = models.IntegerField()
    blue_team_ban2 = models.IntegerField()
    blue_team_ban3 = models.IntegerField()
    blue_team_ban4 = models.IntegerField()
    blue_team_ban5 = models.IntegerField()

    # red team details
    red_team_id = models.IntegerField()
    red_team_baron_kills = models.IntegerField()
    red_team_dragon_kills = models.IntegerField()
    red_team_tower_kills = models.IntegerField()
    red_team_rift_herald = models.IntegerField()
    red_team_ban1 = models.IntegerField()
    red_team_ban2 = models.IntegerField()
    red_team_ban3 = models.IntegerField()
    red_team_ban4 = models.IntegerField()
    red_team_ban5 = models.IntegerField()


class Player(models.Model):

    # summoner stats
    player_id = models.IntegerField()
    team_id = models.IntegerField()
    champion_id = models.IntegerField()
    summoner1_id = models.IntegerField()
    summoner2_id = models.IntegerField()

    # gameplay stats
    item0 = models.IntegerField()
    item1 = models.IntegerField()
    item2 = models.IntegerField()
    item3 = models.IntegerField()
    item4 = models.IntegerField()
    item5 = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    largest_killing_spree = models.IntegerField()
    largest_multi_kill = models.IntegerField()
    double_kills = models.IntegerField()
    triple_kills = models.IntegerField()
    quadra_kills = models.IntegerField()
    penta_kills = models.IntegerField()




