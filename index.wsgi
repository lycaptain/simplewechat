# -*- coding: utf-8 -*-
import os
import sae
import web
import web.db
from weixinInterface import WeixinInterface
from model import *

    
urls = (
'/oj', 'oj',    
'/weixin', 'WeixinInterface',
)

class oj:
    def GET(self):
        ojs = db.select('oj_contest')
        return render.ojfk(ojs)
    
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


    
app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)   
    
    
    
    
    
    