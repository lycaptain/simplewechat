# -*- coding: utf-8 -*-
import urllib2
import json
def simsimi(ask):
    ask = ask.encode('UTF-8')
    qask = urllib2.quote(ask)
    send_headers = {
    'Cookie':'Filtering=0.0; Filtering=0.0; isFirst=1; isFirst=1; simsimi_uid=50840753; simsimi_uid=50840753; teach_btn_url=talk; teach_btn_url=talk; sid=s%3AzwUdofEDCGbrhxyE0sxhKEkF.1wDJhD%2BASBfDiZdvI%2F16VvgTJO7xJb3ZZYT8yLIHVxw; selected_nc=zh; selected_nc=zh; menuType=web; menuType=web; __utma=119922954.2139724797.1396516513.1396516513.1396703679.3; __utmc=119922954; __utmz=119922954.1396516513.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
    }
    baseurl = r'http://www.simsimi.com/func/reqN?lc=zh&ft=0.0&req='
    url = baseurl+qask
    #baseurl = r'http://sandbox.api.simsimi.com/request.p?key=45afcfa5-395f-4676-836d-0a61af189161&lc=en&ft=1.0&text='
    #url = baseurl + qask
    req = urllib2.Request(url,headers=send_headers)
    resp = urllib2.urlopen(req)
    #resp = urllib2.urlopen(url)
    respjson = json.loads(resp.read())
    return respjson