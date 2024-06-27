"""
All Players API Interactions on the free tier.

- Get Players Honours.
- Get Player Milestones.
- Get Player Former Teams.
- Get Player Contracts.
"""

from __future__ import absolute_import
import thesportsdb.settings as TSD
from thesportsdb.requests import make_request


def playerHonours(player_id: str):
    """
    Get the list of honours for this player identified by the `player_id`.
    """
    return make_request(TSD.PLAYER_HONOURS, id=player_id)


def playerMilestones(player_id: str):
    """
    Get the list of milestones for this player identified by the `player_id`.
    """
    return make_request(TSD.PLAYER_MILESTONES, id=player_id)


def playerContracts(player_id: str):
    """
    Get the list of contracts for this player identified by the `player_id`.
    """
    return make_request(TSD.PLAYER_CONTRACTS, id=player_id)


def playerFormerTeams(player_id: str):
    """
    Get the list of former teams for this player identified by the `player_id`.
    """
    return make_request(TSD.PLAYER_FORMER_TEAMS, id=player_id)
