# -*- coding: utf-8 -*-
import os
import sae
import web
from weixinInterface import WeixinInterface
import web.db
import sae.const


db = web.database(
	dbn = 'mysql',
    user = sae.const.MYSQL_USER,
    pwd = sae.const.MYSQL_PASS,
    host = sae.const.MYSQL_HOST,
    port=int(sae.const.MYSQL_PORT)
)

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
    
    
    
    
    
    