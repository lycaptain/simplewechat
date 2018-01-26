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
 '/update','update',
)

class oj:
    def GET(self):
        
        ojs = db.select('oj_contest')
        return render.ojfk(ojs)

class update:
    def GET(self):
        status = '200 OK'
        response_headers = [('Content-type','text/plain')]
        write = start_response(status,response_headers)
 		return ['Hello world']
    
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


    
app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)   
    
    
    
    
    
    