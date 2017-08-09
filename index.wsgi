# coding: UTF-8
import os

import sae
import web
#from translation import Translation
from weixinInterface import WeixinInterface

urls = (
'/wexin','WeixinInterface'
)

sae.add_vendor_dir('vendor')
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)