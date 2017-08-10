# -*- coding: utf-8 -*-
import urllib2
import json
def simsimi(ask):
    ask = ask.encode('UTF-8')
    qask = urllib.request.quote(ask)
    baseurl = r'http://sandbox.api.simsimi.com/request.p?key=45afcfa5-395f-4676-836d-0a61af189161&lc=en&ft=1.0&text='
    url = baseurl + qask
    resp = urllib.request.urlopen(url)
    respjson = json.loads(resp.read().decode())
    return respjson