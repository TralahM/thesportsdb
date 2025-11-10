"""Test cases for events module."""

from unittest.mock import Mock

import pytest

from thesportsdb.events import leagueSeasonEvents


@pytest.fixture
def mock_request(monkeypatch):
    """Create a mock for the make_request function."""
    mock = Mock()
    monkeypatch.setattr("thesportsdb.events.make_request", mock)
    return mock


def test_league_season_events(mock_request):
    """Test getting events for a league and season."""
    mock_request.return_value = {"events": [{"strEvent": "Arsenal vs Chelsea"}]}
    result = leagueSeasonEvents("4328", "2021-2022")
    mock_request.assert_called_with("/eventsseason.php", id="4328", s="2021-2022")
    assert result["events"][0]["strEvent"] == "Arsenal vs Chelsea"


def test_league_season_events_with_different_parameters(mock_request):
    """Test leagueSeasonEvents with different league and season parameters."""
    mock_request.return_value = {
        "events": [{"strEvent": "Liverpool vs Manchester City"}]
    }
    result = leagueSeasonEvents("4329", "2020-2021")
    mock_request.assert_called_with("/eventsseason.php", id="4329", s="2020-2021")
    assert result["events"][0]["strEvent"] == "Liverpool vs Manchester City"


def test_league_season_events_empty_response(mock_request):
    """Test leagueSeasonEvents when API returns empty result."""
    mock_request.return_value = {"events": None}
    result = leagueSeasonEvents("4328", "2021-2022")
    mock_request.assert_called_with("/eventsseason.php", id="4328", s="2021-2022")
    assert result["events"] is None
