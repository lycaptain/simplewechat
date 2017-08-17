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
    'Cookie':'dotcom_session_key=s%3A8W3ACqIiGX5WMBNLDEWj1OtwYcmduVlS.E4EHBpJgnHeqz7KFp5MdUlIHUggYblzDGI3gZG2e8Ck; normalProb=4; lc=ch; currentChatCnt=3; _ga=GA1.2.1265999218.1502948173; _gid=GA1.2.1301977380.1502948173; _gat=1'
    }
    baseurl = r'http://www.simsimi.com/getRealtimeReq?lc=ch&ft=1&normalProb=4&reqText='
    url = baseurl + enask + u"&status=W&talkCnt=3"
    req = urllib2.Request(url,headers=send_headers)
    resp = urllib2.urlopen(req)
    reson = json.loads(resp.read())
    return reson