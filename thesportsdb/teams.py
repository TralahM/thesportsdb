"""
All Teams API Interactions on the free tier.

- Get teams for League.
- Get team Info by ID.
"""

from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def leagueTeams(league_id: str):
    """
    Get all teams for the league identified by the `league_id`.
    """
    return make_request(TSD.LEAGUE_TEAMS, id=league_id)


def teamInfo(team_id: str):
    """
    Get the information for this team identified by the `team_id`.
    """
    return make_request(TSD.TEAM, id=team_id)


def listPlayers(team_id: str):
    """
    Get the list of players for this team identified by the `team_id`.
    """
    return make_request(TSD.TEAM_PLAYERS, id=team_id)


def nextEvents(team_id: str):
    """
    Get the next 5 events for this team identified by the `team_id`.
    """
    return make_request(TSD.NEXT_EVENTS, id=team_id)


def lastEvents(team_id: str):
    """
    Get the last 5 events for this team identified by the `team_id`.
    """
    return make_request(TSD.LAST_EVENTS, id=team_id)
