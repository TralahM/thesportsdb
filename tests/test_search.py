"""Test cases for search module."""

import pytest
from unittest.mock import Mock
from thesportsdb.search import (
    searchTeam,
    searchTeamByCode,
    searchPlayersByTeam,
    searchPlayer,
    searchEvent,
    searchEventByFilename,
    searchVenue,
    searchUserLoves
)

@pytest.fixture
def mock_request(monkeypatch):
    """Create a mock for the make_request function."""
    mock = Mock()
    monkeypatch.setattr('thesportsdb.search.make_request', mock)
    return mock

def test_search_team(mock_request):
    """Test searching for a team by name."""
    mock_request.return_value = {"teams": [{"strTeam": "Arsenal"}]}
    result = searchTeam("Arsenal")
    mock_request.assert_called_with("/searchteams.php", t="Arsenal")
    assert result["teams"][0]["strTeam"] == "Arsenal"

def test_search_team_by_code(mock_request):
    """Test searching for a team by short code."""
    mock_request.return_value = {"teams": [{"strTeam": "Arsenal"}]}
    result = searchTeamByCode("ARS")
    mock_request.assert_called_with("/searchteams.php", sname="ARS")
    assert result["teams"][0]["strTeam"] == "Arsenal"

def test_search_players_by_team(mock_request):
    """Test searching for players by team name."""
    mock_request.return_value = {"player": [{"strPlayer": "Pierre-Emerick Aubameyang"}]}
    result = searchPlayersByTeam("Arsenal")
    mock_request.assert_called_with("/searchplayers.php", t="Arsenal")
    assert result["player"][0]["strPlayer"] == "Pierre-Emerick Aubameyang"

def test_search_player(mock_request):
    """Test searching for a player by name."""
    mock_request.return_value = {"player": [{"strPlayer": "Aubameyang"}]}
    result = searchPlayer("Aubameyang")
    mock_request.assert_called_with("/searchplayers.php", p="Aubameyang")
    assert result["player"][0]["strPlayer"] == "Aubameyang"

def test_search_player_with_team(mock_request):
    """Test searching for a player by name and team."""
    mock_request.return_value = {"player": [{"strPlayer": "Aubameyang"}]}
    result = searchPlayer("Aubameyang", "Arsenal")
    mock_request.assert_called_with("/searchplayers.php", p="Aubameyang", t="Arsenal")
    assert result["player"][0]["strPlayer"] == "Aubameyang"

def test_search_event(mock_request):
    """Test searching for an event by name."""
    mock_request.return_value = {"event": [{"strEvent": "Arsenal vs Chelsea"}]}
    result = searchEvent("Arsenal_vs_Chelsea")
    mock_request.assert_called_with("/searchevents.php", e="Arsenal_vs_Chelsea")
    assert result["event"][0]["strEvent"] == "Arsenal vs Chelsea"

def test_search_event_with_season(mock_request):
    """Test searching for an event by name and season."""
    mock_request.return_value = {"event": [{"strEvent": "Arsenal vs Chelsea"}]}
    result = searchEvent("Arsenal_vs_Chelsea", "2020-2021")
    mock_request.assert_called_with("/searchevents.php", e="Arsenal_vs_Chelsea", s="2020-2021")
    assert result["event"][0]["strEvent"] == "Arsenal vs Chelsea"

def test_search_event_by_filename(mock_request):
    """Test searching for an event by filename."""
    mock_request.return_value = {"event": [{"strEvent": "Arsenal vs Chelsea"}]}
    filename = "English_Premier_League_2015-04-26_Arsenal_vs_Chelsea"
    result = searchEventByFilename(filename)
    mock_request.assert_called_with("/searchfilename.php", e=filename)
    assert result["event"][0]["strEvent"] == "Arsenal vs Chelsea"

def test_search_venue(mock_request):
    """Test searching for a venue by name."""
    mock_request.return_value = {"venues": [{"strVenue": "Emirates Stadium"}]}
    result = searchVenue("Emirates")
    mock_request.assert_called_with("/searchvenues.php", t="Emirates")
    assert result["venues"][0]["strVenue"] == "Emirates Stadium"

def test_search_user_loves(mock_request):
    """Test searching for a user's loved items."""
    mock_request.return_value = {"players": [{"strPlayer": "Aubameyang"}]}
    result = searchUserLoves("testuser")
    mock_request.assert_called_with("/searchloves.php", u="testuser")
    assert result["players"][0]["strPlayer"] == "Aubameyang"
