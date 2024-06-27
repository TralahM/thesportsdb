"""
Module to Provide Functionality for Making requests to the API.
"""

from __future__ import absolute_import
import thesportsdb.settings as TSD
import requests


def _make_url(endpoint: str) -> str:
    """
    Make the full URL for the request.

    :param endpoint: The API endpoint to request
    :return: The full URL for the request
    """
    return TSD.BASE_URL + TSD.API_KEY + endpoint


def make_request(endpoint: str, **kwargs):
    """
    Make a request to the TheSportsDB API endpoint and return a json response.

    :param endpoint: The API endpoint to request
    :param kwargs: Additional parameters to pass to the request
    :return: json response
    """
    params = kwargs
    URL = _make_url(endpoint)
    response = requests.get(URL, params=params)
    try:
        data = response.json()
        return data
    except requests.JSONDecodeError:
        return response.content.decode()
