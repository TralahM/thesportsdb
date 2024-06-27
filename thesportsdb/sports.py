"""
All Sports API Interactions on the free tier.

- Get All Sports.
- Get Sport Info.
- Get TeamVsTeam Sports.
- Get NONTeamVsTeam Sports.
"""
from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def allSports():
    """
    Get all sports provided by the API.
    """
    return make_request(TSD.ALL_SPORTS)


def sportInfo(sport_id: str):
    """
    Get the sport information for the sport identified by `sport_id`.
    """
    return TSD.SPORTS.get(sport_id, None)


def TeamVsTeamSports():
    """
    Get all sports that have the Team Vs Team Format.
    """
    return {"sports": [sportInfo(sp) for sp in TSD.TVTSPORTS]}


def nonTeamVsTeamSports():
    """
    Get all sports that DO NOT have the Team Vs Team Format.
    """
    return {"sports": [sportInfo(sp) for sp in TSD.NONTVTSPORTS]}
