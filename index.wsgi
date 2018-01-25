# -*- coding: utf-8 -*-
import os
import sae
import web
import model 
from weixinInterface import WeixinInterface

class Hello:
    def GET(self):
        return render.hello("hey")
    
class oj:
    def GET(self):
        ccpcs = db.select('ccpc_contest')
        icpcs = db.select('icpc_contest')
        ojs = db.select('oj_contest')
        return render.ojfk(ccpcs, icpcs, ojs)
    
urls = (
'/', 'Hello',
'/weixin', 'WeixinInterface',
'/oj', 'oj',    
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


    
app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)   
    
    
    
    
    
    