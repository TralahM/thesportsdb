"""
All Sports API Interactions on the free tier.

Get All Sports.
Get Sport Info.
Get TeamVsTeam Sports.
Get NONTeamVsTeam Sports.
"""
from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def allSports():
    return make_request(TSD.ALL_SPORTS)
    ...


def sportInfo(sport_id: str):
    return TSD.SPORTS.get(sport_id, None)
    ...


def TeamVsTeamSports():
    return {"sports": [sportInfo(sp) for sp in TSD.TVTSPORTS]}
    ...


def nonTeamVsTeamSports():
    return {"sports": [sportInfo(sp) for sp in TSD.NONTVTSPORTS]}
    ...
