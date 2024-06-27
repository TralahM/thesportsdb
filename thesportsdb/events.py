"""
All Event API interactions on the free tier.

- Get Next 15 Events for league.

- Get Last 15 Events for league.

- Lookup Event Info.

- Fetch Event Results by its ID.

- Get Events for League during a particular Season.
"""

from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def nextLeagueEvents(league_id: str):
    """
    Get the next 15 Events for this league identified by the `league_id`.
    """
    return make_request(TSD.LEAGUE_NEXT_EVENTS, id=league_id)


def lastLeagueEvents(league_id: str):
    """
    Get the last 15 Events for this league identified by the `league_id`.
    """
    return make_request(TSD.LEAGUE_LAST_EVENTS, id=league_id)


def leagueSeasonEvents(league_id: str, season: str):
    """
    Get the  Events for this league identified by the `league_id` for the
    `season` specified.
    """
    return make_request(TSD.LEAGUE_SEASON_EVENTS, l=league_id, s=season)


def leagueSeasonRoundEvents(league_id: str, season: str, round: str):
    """
    Get the  Events for this league identified by the `league_id` for the
    `season` and `round` specified.

    :param league_id: League ID
    :param season: Season
    :param round: Round
    :return: json response
    """
    return make_request(
        TSD.LEAGUE_SEASON_ROUND_EVENTS,
        l=league_id,
        s=season,
        r=round,
    )


def eventResult(event_id: str):
    """
    Get the Event Results for this event specified by the `event_id`.

    :param event_id: Event ID
    :return: json response
    """
    return make_request(TSD.EVENT_RESULT, id=event_id)


def eventInfo(event_id: str):
    """
    Get the Event Details for this event specified by the `event_id`.

    :param event_id: Event ID
    :return: json response

    .. literalinclude:: event_info.json
       :language: JSON
    """
    return make_request(TSD.EVENT, id=event_id)


def eventStats(event_id: str):
    """
    Get the Event Stats for this event specified by the `event_id`.

    :param event_id: Event ID
    :return: json response
    """
    return make_request(TSD.EVENT_STATS, id=event_id)


def eventLineups(event_id: str):
    """
    Get the Event Lineups for this event specified by the `event_id`.

    :param event_id: Event ID
    :return: json response
    """
    return make_request(TSD.EVENT_LINEUPS, id=event_id)


def eventTimeline(event_id: str):
    """
    Get the Event Timeline for this event specified by the `event_id`.

    :param event_id: Event ID
    :return: json response
    """
    return make_request(TSD.EVENT_TIMELINE, id=event_id)


def eventTv(event_id: str):
    """
    Get the Event TVT for this event specified by the `event_id`.

    :param event_id: Event ID
    :return: json response
    """
    return make_request(TSD.TV_EVENT, id=event_id)


def eventsDay(day: str, **kwargs):
    """
    Get the Events for this day specified by the `day`.

    :param day: Date in YYYY-MM-DD format
    :param kwargs: Additional parameters to pass to the request e.g, s=Soccer for sport and/or l=4328 league id
    :return: json response

    """
    return make_request(TSD.EVENTS_DAY, d=day, **kwargs)


def venueInfo(venue_id: str):
    """
    Get the Venue Details for this venue specified by the `venue_id`.

    :param venue_id: Venue ID
    :return: json response
    """
    return make_request(TSD.VENUE, id=venue_id)
