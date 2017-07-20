# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2, json
from lxml import etree

class WeixinInterface:
    
    def _init_(self):
        self.app_root = os.path.dirname(_file_)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        
    def GET(self):
        #获取输入参数
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        
        #自己的token
        token = "41512241"
        
        #字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.uodate, list)
        hashcode = sha1.hexdigest()
        #sha1加密算法
        
        #如果是来自微信服务端的请求则回复echostr
        if hashcode == signature:
            return echostr
        
        def POST(self):
            str_xml = web.data() #获得POST来的数据
            xml = etree.fromstring(str_xml) #进行xml解析
            content = xml.find("Content").text #获取用户输入内容
            msgType = xml.find("MsgType").text
            fromUser = xml.find("FromUserName").text
        	toUser = xml.find("ToUserName").text
            return self.render.reply_text(fromUser, toUser, int(time.time()),content)
        