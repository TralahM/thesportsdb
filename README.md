
[![Build Status](https://travis-ci.com/TralahM/thesportsdb.svg?branch=master)](https://travis-ci.com/TralahM/thesportsdb)
[![Build status](https://ci.appveyor.com/api/projects/status/yvvmq5hyf7hj743a?svg=true)](https://ci.appveyor.com/project/TralahM/thesportsdb)
[![Build status](https://ci.appveyor.com/api/projects/status/yvvmq5hyf7hj743a/branch/master?svg=true)](https://ci.appveyor.com/project/TralahM/thesportsdb/branch/master)
[![Documentation Status](https://readthedocs.org/projects/thesportsdb/badge/?version=latest)](https://thesportsdb.readthedocs.io/en/latest/?badge=latest)
[![License: GPLV3](https://img.shields.io/badge/License-GPLV2-green.svg)](https://opensource.org/licenses/GPLV2)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![Views](http://hits.dwyl.io/TralahM/thesportsdb.svg)](http://dwyl.io/TralahM/thesportsdb)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/thesportsdb/pull/)
[![GitHub pull-requests](https://img.shields.io/badge/Issues-pr-red.svg?style=flat-square)](https://github.com/TralahM/thesportsdb/pull/)
[![Language](https://img.shields.io/badge/Language-python-3572A5.svg)](https://github.com/TralahM)

# TheSportsDB Python SDK.

Unofficial Python API client wrapper package around [TheSportsDB API](https://thesportsdb.com) .
An open, crowd-sourced database of sports artwork and metadata with a free API.


[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge)](https://github.com/TralahM)

# Documentation

[![Documentation](https://img.shields.io/badge/Docs-thesportsdb-blue.svg?style=for-the-badge)](https://thesportsdb.readthedocs.io/en/latest/)

# How to Install

```bash
# In terminal do:
$ pip install thesportsdb
```

## Building from Source for Developers

```console
$ git clone https://github.com/TralahM/thesportsdb.git
$ cd thesportsdb
$ python setup.py build
$ pip install -e .
```

# QuickStart

```python

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
## print(thesportsdb)

```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE

[Read the LICENSE here](LICENSE)


# Self-Promotion

[![TralahM](https://img.shields.io/badge/Twitter-TralahM-blue.svg?style=for-the-badge)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Github-TralahM-black.svg?style=for-the-badge)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-red.svg?style=for-the-badge)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge)](https://tralahm.tralahtek.com)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://tralahtek.com)


