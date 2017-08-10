# -*- coding: utf-8 -*-
import urllib2

def simsimi(ask):
    ask = ask.encode('UTF-8')
    qask = urllib2.quote(ask)
    baseurl = r'http://www.simsimi.com/func/req?msg='
    url = baseurl + qask + '&lc=ch&ft=0.0'
    resp = urllib2.urlopen(url)
    respjson = json.loads(resp.read())
    return respjson