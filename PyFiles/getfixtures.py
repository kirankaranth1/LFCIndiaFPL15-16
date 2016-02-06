#!/usr/bin/env python
from __future__ import print_function
import re
import requests
from lxml import html
from StringIO import StringIO
import sys
import os
import json
import math

def getfix(gw):
    res = requests.get("http://www.football-data.org/soccerseasons/398/fixtures?matchday="+str(gw))
    result=json.loads(res.text)
    return result['fixtures']

template = "%25s vs %25s"
fixtures = getfix(20)
for f in fixtures:
    print('{0: <24} vs {1: >25}'.format(f['homeTeamName'],f['awayTeamName']))
 
