"""
All Teams API Interactions on the free tier.

Get teams for League.
Get team Info by ID.
"""
from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def leagueTeams(league_id: str):
    return make_request(TSD.LEAGUE_TEAMS, id=league_id)
    ...


def teamInfo(team_id: str):
    return make_request(TSD.TEAM, id=team_id)
    ...
