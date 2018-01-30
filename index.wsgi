# -*- coding: utf-8 -*-
import os
import sae
import web
import web.db
from weixinInterface import WeixinInterface
from model import *
sae.add_vendor_dir('requests')
    
urls = (
'/oj', 'oj',    
'/weixin', 'WeixinInterface',
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


    
app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)   
    
    
    
    
    
    