Overview
-------------

Installation
++++++++++++++++++++

.. code-block:: bash

  pip install thesportsdb



QuickStart
---------------

By default the library will use the free TheSportsDB API. To use the premium
version you need to register at https://thesportsdb.com/ and get an API key.

Then you can set the API key to be used by the library as a shell environment
variable using ``export THESPORTSDB_API_KEY=YOUR_API_KEY`` before using the library.

Usage
++++++++++++++++++++

.. code-block:: python

   import thesportsdb
   event_info=thesportsdb.events.eventInfo("1008672")
   event_result=thesportsdb.events.eventResult("1008695")
   previous_events=thesportsdb.events.lastLeagueEvents("4328")
   events_for_league_season20192020=thesportsdb.events.leagueSeasonEvents("4328", "2019-2020")
   upcoming_soccer_events=thesportsdb.events.nextLeagueEvents("4328")
   all_countries=thesportsdb.countries.allCountries()
   all_leagues=thesportsdb.leagues.allLeagues()
   EPL_info=thesportsdb.leagues.leagueInfo("4328")
   EPL_standings=thesportsdb.leagues.leagueSeasonTable("4328", "2019-2020")
   soccer_leagues=thesportsdb.leagues.sportLeagues("102")
   Team_sports=thesportsdb.sports.TeamVsTeamSports()
   all_sports=thesportsdb.sports.allSports()
   nonTeamSports=thesportsdb.sports.nonTeamVsTeamSports()
   sport_details=thesportsdb.sports.sportInfo("102")
   EPL_teams=thesportsdb.teams.leagueTeams("4328")
   team_details_ManC=thesportsdb.teams.teamInfo("133613")



Head to  the `API Reference <api.html>`_ for more details.
