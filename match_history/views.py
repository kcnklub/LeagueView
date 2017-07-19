from django.shortcuts import render
from .LeagueParser import MatchHistoryParser, AccountParser
from .models import Account

# Create your views here.


def index(request):
    data = {}
    return render(request, 'match_history/index.html', data)


def detail(request, game_id):
    match_parser = MatchHistoryParser('RGAPI-f2866403-5bfd-4ab7-a756-92a17ad3488b', 'na1')
    match = match_parser.get_match_details(game_id)
    blue_team = match['teams'][0]
    red_team = match['teams'][1]
    print(blue_team)
    print(red_team)
    data = {
        'match_info': game_id,
        'blue_team': blue_team,
        'red_team': red_team
    }
    return render(request, 'match_history/match_details.html', data)


def search_summoner(request):
    summoner_name = request.POST.get('summoner_name', '')
    try:
        try_summoner = Account.objects.get(summoner_name=summoner_name)
    except Account.DoesNotExist:
        # add the user that was not found to the database.
        account_parser = AccountParser('RGAPI-f2866403-5bfd-4ab7-a756-92a17ad3488b', 'na1')
        account_parser.get_account_by_summoner_name(request.POST['summoner_name'])
        # get the user that was just added to the database to get their match history
        searched_summoner = Account.objects.get(summoner_name=summoner_name)
        match_parser = MatchHistoryParser('RGAPI-f2866403-5bfd-4ab7-a756-92a17ad3488b', 'na1')
        match_parser.get_match_history(searched_summoner.get_account_id())
        match_history = match_parser.convert_match_data()
        data = {'match_history': match_history}
        return render(request, 'match_history/index.html', data)
    except KeyError:
        return render(request, 'match_history/index.html', {
            "error_message": "There have been an error searching of that summoner"
        })
    else:
        searched_summoner = Account.objects.get(summoner_name=summoner_name)
        match_parser = MatchHistoryParser('RGAPI-f2866403-5bfd-4ab7-a756-92a17ad3488b', 'na1')
        match_parser.get_match_history(searched_summoner.get_account_id())
        match_history = match_parser.convert_match_data()
        data = {'match_history': match_history}
        return render(request, 'match_history/index.html', data)

