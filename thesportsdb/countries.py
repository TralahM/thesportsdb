"""
All Countries API interactions.

- Get all Countries.
- List all Leagues in a country (limited 50 on free tier)
"""

from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def allCountries():
    """
    Get all countries information.
    """
    return make_request(TSD.ALL_COUNTRIES)


def listLeaguesByCountry(country_id: str, **kwargs):
    """
    List all Leagues in a country (limited 50 on free tier).

    :param country_id: ID of the country e.g England
    :param kwargs: Additional parameters to pass to the request e.g s=Soccer for soccer
    :return: json response
    """
    return make_request(TSD.LEAGUES_BY_COUNTRY, c=country_id, **kwargs)
