import datetime
import dateutil.parser

from django.shortcuts import render

from . import services


def index(request):
    return render(request, 'index.html' )

def all_games(request):
    sdk = services.OpenLigaSDK()
    all_games = sdk.get_all_games()

    context = {'all_games' : all_games}
    return render(request, 'all_games.html', context)

def next_day_games(request):
    sdk = services.OpenLigaSDK()
    all_games = sdk.get_all_games()

    next_day_games = []
    for game in all_games:
        # next_day_games.append(game['MatchDateTimeUTC'])
        dt_str = game['MatchDateTimeUTC']
        dt_iso = dateutil.parser.isoparse(dt_str)
        dt_game = datetime.date(dt_iso.year, dt_iso.month, dt_iso.day)
        # print('dt_game: ' + str(dt_game))
        # dt_today = datetime.date.today()
        dt_today = datetime.date(2021, 8, 13)
        # print('today: ' + str(dt_today))
        dt_tomorrow = dt_today + datetime.timedelta(days = 1)
        # print('dt_tomorrow: ' + str(dt_tomorrow))

        if dt_game == dt_tomorrow:
            next_day_games.append(game)

    context = {'next_day_games': next_day_games}
    return render(request, 'next_day_games.html', context)

def next_game_day(request):
    # Next upcoming matches (following Gameday)
    pass

def win_loss_ratio(request):
    # get_all_teams
    sdk = services.OpenLigaSDK()
    all_teams = sdk.get_all_teams()

    statistic = dict()
    for team in all_teams:
        statistic[team['TeamId']] = {
            'team_name': team['TeamName'],
            'wins': 0,
            'loss': 0,
        }

    # get_all_matches
    all_games = sdk.get_all_games()
    for game in all_games:
        if not game['MatchIsFinished']:
            continue

        team1_id = game['Team1']['TeamId']
        team2_id = game['Team2']['TeamId']

        if game['MatchResults']:
            team1_goals = int(game['MatchResults'][0]['PointsTeam1'])
            team2_goals = int(game['MatchResults'][0]['PointsTeam2'])

            if team1_goals > team2_goals:
                statistic[team1_id]['wins'] += 1
                statistic[team2_id]['loss'] += 1
            elif team1_goals < team2_goals:
                statistic[team1_id]['loss'] += 1
                statistic[team2_id]['wins'] += 1
            else:
                pass
        else:
            pass

    for k,v in statistic.items():
        ratio = v['wins'] / v['loss']
        statistic[k]['win_ratio'] = str(round(ratio, 2))

    statistic_sorted = _sorter(statistic)
    print(statistic_sorted)

    context = {'statistic': statistic_sorted}
    return render(request, 'win_loss_ratio.html' , context)

def _sorter(d):
    return sorted(d.items(), key=lambda x: x[1]['win_ratio'], reverse=True)
