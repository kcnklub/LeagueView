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
    mode = models.CharField(max_length=30, null=True)

    # can determine red teams also
    blue_team_win = models.CharField(max_length=10)
    blue_team_first_blood = models.NullBooleanField()
    blue_team_first_tower = models.NullBooleanField()
    blue_team_first_inhib = models.NullBooleanField()
    blue_team_first_baron = models.NullBooleanField()
    blue_team_first_herald = models.NullBooleanField()

    # blue team details
    blue_team_id = models.IntegerField(null=True)
    blue_team_baron_kills = models.IntegerField(null=True)
    blue_team_dragon_kills = models.IntegerField(null=True)
    blue_team_tower_kills = models.IntegerField(null=True)
    blue_team_rift_herald = models.IntegerField(null=True)
    blue_team_ban1 = models.IntegerField(null=True)
    blue_team_ban2 = models.IntegerField(null=True)
    blue_team_ban3 = models.IntegerField(null=True)
    blue_team_ban4 = models.IntegerField(null=True)
    blue_team_ban5 = models.IntegerField(null=True)

    # red team details
    red_team_id = models.IntegerField(null=True)
    red_team_baron_kills = models.IntegerField(null=True)
    red_team_dragon_kills = models.IntegerField(null=True)
    red_team_tower_kills = models.IntegerField(null=True)
    red_team_rift_herald = models.IntegerField(null=True)
    red_team_ban1 = models.IntegerField(null=True)
    red_team_ban2 = models.IntegerField(null=True)
    red_team_ban3 = models.IntegerField(null=True)
    red_team_ban4 = models.IntegerField(null=True)
    red_team_ban5 = models.IntegerField(null=True)

    def __str__(self):
        return str(self.game_id)


class Player(models.Model):

    # summoner stats
    participant_id = models.IntegerField()
    team_id = models.IntegerField()
    game_id = models.IntegerField()
    champion_id = models.IntegerField()
    summoner1_id = models.IntegerField()
    summoner2_id = models.IntegerField()
    summoner_id = models.IntegerField(null=True)

    # gameplay stats
    item0 = models.IntegerField(null=True)
    item1 = models.IntegerField(null=True)
    item2 = models.IntegerField(null=True)
    item3 = models.IntegerField(null=True)
    item4 = models.IntegerField(null=True)
    item5 = models.IntegerField(null=True)
    item6 = models.IntegerField(null=True)
    kills = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    largest_killing_spree = models.IntegerField(null=True)
    largest_multi_kill = models.IntegerField(null=True)
    double_kills = models.IntegerField(null=True)
    triple_kills = models.IntegerField(null=True)
    quadra_kills = models.IntegerField(null=True)
    penta_kills = models.IntegerField(null=True)

    def __str__(self):
        return str(self.game_id) + " - " + str(self.participant_id)




