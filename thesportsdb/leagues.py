"""
All League related API interactions on the free tier.

Get All Leagues.
Get League Info.
Get Leagues for Sport.
Get Table for League at a particular Season.
"""
from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def allLeagues():
    return make_request(TSD.ALL_LEAGUES)
    ...


def leagueSeasonTable(league_id: str, season: str):
    return make_request(TSD.LEAGUE_SEASON_TABLE, l=league_id, s=season)
    ...


def leagueInfo(league_id: str):
    return TSD.LEAGUE_MAP.get(league_id)
    ...


def sportLeagues(sport_id: str):
    return {"leagues": TSD.SPORTS_LEAGUES_MAP.get(sport_id, None)}
    ...
