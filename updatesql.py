# -*- coding: utf-8 -*-
import model
import requests
import re
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree
import urllib,urllib2
import json
oj_url = 'http://contests.acmicpc.info/contests.json'
OJ_json = requests.get(oj_url).text
OJ = json.loads(OJ_json)
OJS = []
id = 0
for num in OJ:
    OJS.append((id, num['oj'], num['link'], num['name'], num['start_time'], num['week'], num['access']))
    id = id+1
model.delectoj()
for num in OJS:
    model.upoj(num[0], num[1], num[2], num[3], num[4], num[5], num[6])
