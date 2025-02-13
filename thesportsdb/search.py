"""
Search API interactions on the free tier.

- Search for team by name
- Search for team by short code
- Search for players by name or team
- Search for events by name
- Search for events by filename
- Search for venues by name
"""

from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def searchTeam(team_name: str):
    """
    Search for a team by name.
    
    :param team_name: Team name to search for
    :return: json response
    """
    return make_request("/searchteams.php", t=team_name)


def searchTeamByCode(short_code: str):
    """
    Search for a team by short code.
    
    :param short_code: Team short code (e.g. 'ARS' for Arsenal)
    :return: json response
    """
    return make_request("/searchteams.php", sname=short_code)


def searchPlayersByTeam(team_name: str):
    """
    Search for all players from a team.
    
    :param team_name: Team name to get players for
    :return: json response
    """
    return make_request("/searchplayers.php", t=team_name)


def searchPlayer(player_name: str, team_name: str = None):
    """
    Search for players by name, optionally filtered by team.
    
    :param player_name: Player name to search for
    :param team_name: Optional team name to filter by
    :return: json response
    """
    params = {"p": player_name}
    if team_name:
        params["t"] = team_name
    return make_request("/searchplayers.php", **params)


def searchEvent(event_name: str, season: str = None):
    """
    Search for events by name, optionally filtered by season.
    
    :param event_name: Event name to search for (e.g. 'Arsenal_vs_Chelsea')
    :param season: Optional season to filter by (e.g. '2016-2017')
    :return: json response
    """
    params = {"e": event_name}
    if season:
        params["s"] = season
    return make_request("/searchevents.php", **params)


def searchEventByFilename(filename: str):
    """
    Search for event by event filename.
    
    :param filename: Event filename (e.g. 'English_Premier_League_2015-04-26_Arsenal_vs_Chelsea')
    :return: json response
    """
    return make_request("/searchfilename.php", e=filename)


def searchVenue(venue_name: str):
    """
    Search for venue by name.
    
    :param venue_name: Venue name to search for
    :return: json response
    """
    return make_request("/searchvenues.php", t=venue_name)


def searchUserLoves(username: str):
    """
    List all users loved teams and players.
    
    :param username: Username to get loved items for
    :return: json response
    """
    return make_request("/searchloves.php", u=username)
