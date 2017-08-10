import urllib2
#查询快递

def detect_com(postid):
    r = urllib2.urlopen('http://www.kuaidi100.com/autonumber/autoComNum?text='+postid)
    h = r.read()
    k = eval(h)
    kuaiditpye = k["auto"][0]['comCode']
    return kuaiditpye