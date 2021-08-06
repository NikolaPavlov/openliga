import datetime
import dateutil.parser

from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from . import services


def index(request):
    sdk = services.OpenLigaSDK()
    all_games = sdk.get_all_games()
    next_games = _get_next_game_day()

    context = {
       'all_games' : all_games,
       'next_games': next_games,
    }
    return render(request, 'index.html', context)


def win_loss_ratio(request):
    sdk = services.OpenLigaSDK()
    all_stats = sdk.get_all_stats()

    for s in all_stats:
        s['win_loss'] = _get_ratio(s['Won'], s['Lost'])

    context = { 'statistic': all_stats }

    return render(request, 'win_loss_ratio.html', context)


def team_search(request):
    if 'q' in request.GET:
        team_name = str(request.GET['q'])
        if team_name is not None:
            if _is_team_in_league(team_name):
                next_game = _get_team_next_game(team_name)
                all_games_of_team = _get_team_season_matches(team_name)

                team_stats = _get_team_stats(team_name)
                team_stats['win_loss'] = _get_ratio(team_stats['Won'], team_stats['Lost'])

                context = {
                    'next_game': next_game,
                    'all_games_of_team': all_games_of_team,
                    'team_stats': team_stats,
                    'season': settings.SEASON,
                }
            else:
                err_msg = "['%s'] is not in the league" % team_name
                context = { 'err_msg': err_msg }
            return render(request, 'team_search.html', context)
    return render(request, 'team_search.html')


def _get_next_game_day():
    sdk = services.OpenLigaSDK()
    all_games = sdk.get_all_games()

    first_dt_str = all_games[0]['MatchDateTimeUTC']
    first_date = _dt_str_to_iso(first_dt_str)
    now = timezone.now().date()

    if now > first_date:
        return None

    next_games = []
    for game in all_games:
        game_date = _dt_str_to_iso(game['MatchDateTimeUTC'])
        if game_date == first_date:
            next_games.append(game)

    return next_games


def _dt_str_to_iso(date):
    date_iso = dateutil.parser.isoparse(date)
    date_strip = datetime.date(date_iso.year, date_iso.month, date_iso.day)
    return date_strip


def _is_team_in_league(team):
    sdk = services.OpenLigaSDK()
    all_teams = sdk.get_all_teams()

    all_team_names = []
    for t in all_teams:
        all_team_names.append( (t['TeamName']).lower() )

    if team.lower() in all_team_names:
        return True
    return False


def _get_team_next_game(team_name):
    sdk = services.OpenLigaSDK()
    all_games = sdk.get_all_games()

    for game in all_games:
        team1_name = game['Team1']['TeamName']
        team2_name = game['Team2']['TeamName']
        if team1_name == team_name or team2_name == team_name:
            if game['MatchIsFinished']:
                continue
            return game
    return None


def _get_team_season_matches(team_name):
    sdk = services.OpenLigaSDK()
    all_games = sdk.get_all_games()

    all_games_of_team = []
    for game in all_games:
        team1_name = game['Team1']['TeamName']
        team2_name = game['Team2']['TeamName']
        if team1_name == team_name or team2_name == team_name:
            all_games_of_team.append(game)
    return all_games_of_team


def _get_team_stats(team_name):
    sdk = services.OpenLigaSDK()
    all_stats = sdk.get_all_stats()

    for stats in all_stats:
        if stats['TeamName'] == team_name:
            return stats
    return None


def _get_ratio(win, loss):
    if loss == 0:
        return int(win)
    else:
        return round(float(win / loss), 2)
