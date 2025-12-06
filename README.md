[![Documentation Status](https://readthedocs.org/projects/thesportsdb/badge/?version=latest)](https://thesportsdb.readthedocs.io/en/latest/?badge=latest)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/thesportsdb/pull/)
[![Language](https://img.shields.io/badge/Language-python-3572A5.svg)](https://github.com/TralahM)

# TheSportsDB Python SDK

Unofficial Python API client wrapper package around
[TheSportsDB API](https://thesportsdb.com).
An open, crowd-sourced database of sports artwork and metadata with a free API.

[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge)](https://github.com/TralahM)

# Documentation

[![Documentation](https://img.shields.io/badge/Docs-thesportsdb-blue.svg?style=for-the-badge)](https://thesportsdb.readthedocs.io/en/latest/)

# How to Install

```sh
# In terminal do:

pip install thesportsdb
```

## Building from Source for Developers

```sh
git clone https://github.com/TralahM/thesportsdb.git

cd thesportsdb

python setup.py build

pip install -e .
```

# QuickStart

By default the library will use the free TheSportsDB API. To use the premium
version you need to register at [TheSportsDB](https://thesportsdb.com/)
and get an API key.

Then you can set the API key to be used by the library as a shell environment
variable using `export THESPORTSDB_API_KEY=YOUR_API_KEY` before using the library.

```python

import thesportsdb

event_info = thesportsdb.events.eventInfo("1008672")

event_result = thesportsdb.events.eventResult("1008695")

previous_events = thesportsdb.events.lastLeagueEvents("4328")

events_for_league_season20192020 = thesportsdb.events.leagueSeasonEvents(
    "4328", "2019-2020"
)

upcoming_soccer_events = thesportsdb.events.nextLeagueEvents("4328")

all_countries = thesportsdb.countries.allCountries()

all_leagues = thesportsdb.leagues.allLeagues()

EPL_info = thesportsdb.leagues.leagueInfo("4328")

EPL_standings = thesportsdb.leagues.leagueSeasonTable("4328", "2019-2020")

soccer_leagues = thesportsdb.leagues.sportLeagues("102")

Team_sports = thesportsdb.sports.TeamVsTeamSports()

all_sports = thesportsdb.sports.allSports()

nonTeamSports = thesportsdb.sports.nonTeamVsTeamSports()

sport_details = thesportsdb.sports.sportInfo("102")

EPL_teams = thesportsdb.teams.leagueTeams("4328")

team_details_ManC = thesportsdb.teams.teamInfo("133613")
## print(thesportsdb)
```

# Contributing

[See the Contributing File](CONTRIBUTING.rst)

# LICENCE

[Read the LICENSE here](./LICENSE)

# Self-Promotion

[![TralahM](https://img.shields.io/badge/Twitter-TralahM-blue.svg?style=for-the-badge)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Github-TralahM-black.svg?style=for-the-badge)](https://github.com/TralahM)
