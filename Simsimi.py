# -*- coding: utf-8 -*-
import sys
import os
import urllib2
import json
import hashlib
import lxml
import time
import os
import urllib2
import json
import re
from lxml import etree
def simsimi(ask):
    ask = ask.encode('UTF-8')
    enask = urllib2.quote(ask)
    send_headers = {
    'Cookie':'dotcom_session_key=s%3AGriOh4cD92ITF-VRRsY69PTGniBjNCpd.7KKLzK%2BURsCXZwhYNSCK%2FobHAawD2d8Gos1rgIyGIbQ; _gat=1; normalProb=0; lc=ch; _ga=GA1.2.952018532.1503307364; _gid=GA1.2.203362047.1503307364; currentChatCnt=8'
    }
    baseurl = r'http://www.simsimi.com/getRealtimeReq?lc=ch&ft=1&normalProb=0&reqText='
    url = baseurl + enask + u"&status=W&talkCnt=8"
    req = urllib2.Request(url,headers=send_headers)
    resp = urllib2.urlopen(req)
    reson = json.loads(resp.read())
    return reson