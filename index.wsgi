# -*- coding: utf-8 -*-
import os
import sae
import web
import web.db
from weixinInterface import WeixinInterface
from model import *
    
urls = (
'/weixin', 'WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)   
def token(requset):  
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (Config.AppID, Config.AppSecret)  
   	result = urllib2.urlopen(url).read()  
   	Config.access_token = json.loads(result).get('access_token')  
   	print 'access_token===%s' % Config.access_token  
   	return HttpResponse(result)
    
def createMenu(request):
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % Config.access_toke
    data = {"button":[{"name":"sm","sub_button":[{"type":"click","name":"shengming","key":"sm"}]}]}
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('encoding', 'utf-8')
    response = urllib2.urlopen(req, json.dumps(data,ensure_ascii=False))
    result = response.read()
    return HttpResponse(result)   
    
    
    
    
    