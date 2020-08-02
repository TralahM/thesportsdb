"""
All Event API interactions on the free tier.

Get Next 15 Events for league.
Get Last 15 Events for league.
Lookup Event Info.
Fetch Event Results by its ID.
Get Events for League during a particular Season.
"""
from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def nextLeagueEvents(league_id: str):
    """
    Get the next 15 Events for this league identified by the `league_id`
    """
    return make_request(TSD.LEAGUE_NEXT_EVENTS, id=league_id)
    ...


def lastLeagueEvents(league_id: str):
    """
    Get the last 15 Events for this league identified by the `league_id`
    """
    return make_request(TSD.LEAGUE_LAST_EVENTS, id=league_id)
    ...


def leagueSeasonEvents(league_id: str, season: str):
    """
    Get the  Events for this league identified by the `league_id` for the
    `season` specified.
    """
    return make_request(TSD.LEAGUE_SEASON_EVENTS, l=league_id, s=season)
    ...


def eventResult(event_id: str):
    """
    Get the Event Results for this event specified by the `event_id`
    """
    return make_request(TSD.EVENT_RESULT, id=event_id)
    ...


def eventInfo(event_id: str):
    """
    Get the Event Details for this event specified by the `event_id`
    """
    return make_request(TSD.EVENT, id=event_id)
    ...
