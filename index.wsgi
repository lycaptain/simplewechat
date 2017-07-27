# coding: UTF-8
import os
import sae
import web

from weixinInterface import WeixinInterface

urls = (
'/', 'WeixinInterface'
)

app_root = os.path.dirname(_file_)
templates_root = os.path.join(app_root,'templates')
render = web.template.render(template_root)

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)
