"""
Module to Provide Functionality for Making requests to the API.
"""
from __future__ import absolute_import
import thesportsdb.settings as TSD
import requests


def _make_url(endpoint: str) -> str:
    return TSD.BASE_URL + TSD.API_KEY + endpoint


def make_request(endpoint: str, **kwargs):
    params = kwargs
    URL = _make_url(endpoint)
    response = requests.get(URL, params=params)
    return response.json()
