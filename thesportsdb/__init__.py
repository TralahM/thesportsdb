"""
=======================================================================
:PACKAGE:   thesportsdb
:AUTHOR:	 Tralah M Brian <briantralah@tralahtek.com>
:TWITTER: 	 @TralahM
:GITHUB: 	 <https://github.com/TralahM/thesportsdb>
:COPYRIGHT:  (c) 2020  TralahTek LLC.
:LICENSE: 	 GPLV3 , see LICENSE for more details.
:WEBSITE:	<https://www.tralahtek.com>
:CREATED: 	2020-08-01
=======================================================================

:DESCRIPTION:  TheSportsDB API Python SDK
Unofficial Python SDK  package around TheSportsDB API .
An open, crowd-sourced database of sports artwork and metadata with a free API.

"""

from __future__ import absolute_import

from thesportsdb import (
    countries,
    events,
    leagues,
    players,
    requests,
    settings,
    sports,
    teams,
)

__version__ = "0.3.0"
__author__ = "Tralah M Brian <https://github.com/TralahM/thesportsdb>"
__all__ = [
    countries,
    events,
    leagues,
    requests,
    settings,
    sports,
    teams,
    players,
]
