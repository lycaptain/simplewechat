  # -*- coding: utf-8 -*-
import os
import sae
import web
import DBmodel
from weixinInterface import WeixinInterface

class Hello:
    def GET(self):
        return render.hello("你好")
    
class feedback:
    def GET(self):
        fkcon = DBmodel.get_fkcontent()
        return render.checkfk(fkcon)
    
    
urls = (
'/hi', 'Hello',
'/weixin','WeixinInterface',
'/ck','feedback',
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


    
app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)   
    
    
    
    
    
    