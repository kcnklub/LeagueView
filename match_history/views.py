from django.shortcuts import render
from .LeagueParser import MatchHistoryParser, AccountParser
from .models import Account, Player, Match
from LeagueAPI.MatchTool import MatchTool


# Create your views here.


def index(request):
    data = {}
    return render(request, 'match_history/index.html', data)


def detail(request, game_id):
    test = MatchTool('RGAPI-5ed59bd7-1a5c-4c8e-a645-c3ce4c875f64', 'na1')
    test.save_match(game_id, '212268870')
    return render(request, 'match_history/match_details.html')


def search_summoner(request):
    summoner_name = request.POST.get('summoner_name', '').lower()
    try:
        try_summoner = Account.objects.get(summoner_name=summoner_name)
    except Account.DoesNotExist:
        # add the user that was not found to the database.
        account_parser = AccountParser('RGAPI-5ed59bd7-1a5c-4c8e-a645-c3ce4c875f64', 'na1')
        account_parser.get_account_by_summoner_name(request.POST['summoner_name'])
        # get the user that was just added to the database to get their match history
        searched_summoner = Account.objects.get(summoner_name=summoner_name)
        match_parser = MatchHistoryParser('RGAPI-5ed59bd7-1a5c-4c8e-a645-c3ce4c875f64', 'na1')
        match_parser.get_match_history(searched_summoner.get_account_id())
        match_history = match_parser.convert_match_data()
        data = {
            'summoner': searched_summoner,
            'match_history': match_history
        }
        return render(request, 'match_history/index.html', data)
    except KeyError:
        return render(request, 'match_history/index.html', {
            "error_message": "There have been an error searching of that summoner"
        })
    else:
        searched_summoner = Account.objects.get(summoner_name=summoner_name)
        match_parser = MatchHistoryParser('RGAPI-5ed59bd7-1a5c-4c8e-a645-c3ce4c875f64', 'na1')
        match_parser.get_match_history(searched_summoner.get_account_id())
        match_history = match_parser.convert_match_data()
        data = {
            'summoner': searched_summoner,
            'match_history': match_history
        }
        return render(request, 'match_history/index.html', data)

