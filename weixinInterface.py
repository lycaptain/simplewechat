# -*- coding: utf-8 -*-
import hashlib
import web
import web.db
import lxml
import time
import os
import urllib2,json
import json
import cxkd
import Simsimi
import translation
import pylibmc
import model
from lxml import etree
os.environ['disable_fetchurl'] = "1"

class WeixinInterface:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
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
        token = "anmmd" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list = [token,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode = sha1.hexdigest()
        #sha1加密算法        

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
	
        
    def POST(self): 
        str_xml = web.data() #获得post来的数据 
        xml = etree.fromstring(str_xml)#进行XML解析 
        msgType = xml.find("MsgType").text 
        fromUser = xml.find("FromUserName").text 
        toUser = xml.find("ToUserName").text 
        mc = pylibmc.Client()
        #初始化一个memcache实例来保存用户的操作
        
        if msgType == 'text':
            content=xml.find("Content").text
            if content.startswith('oj'):
                return self.render.reply_text(fromUser,toUser,int(time.time()),u'1.simplewechat.applinzi.com/')
            if content[0:2] == u"快递":
                post = str(content[2:])
                kuaidi = cxkd.detect_com(post)
                return self.render.reply_text(fromUser,toUser,int(time.time()), kuaidi)                                    
            else:
            	if content.lower() == 'bye':
                	mc.delete(fromUser+'_xhj')
                	return self.render.reply_text(fromUser,toUser,int(time.time()),u'您已经跳出了和小黄鸡的交谈中，输入help来显示操作指令')
            	if content.lower() == 'xhj':
                	mc.set(fromUser+'_xhj', 'xhj')
                	return self.render.reply_text(fromUser,toUser,int(time.time()),u'您已经进入与小黄鸡的交谈中，请尽情的蹂躏它吧！输入bye跳出与小黄鸡的交谈')
            	if content.lower() == 'help':
               		replayText = u'''1.输入快递+单号（不含‘+’）查询该快递属于哪一个公司\n2.输入xhj进入调戏小黄鸡模式，输入bye离开小黄鸡\n3.输入其它则进入翻译模式
4 输入 fk空格+反馈内容即可反馈'''
                	return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)

            #读取mcmcache数据
            mcxhj = mc.get(fromUser+'_xhj')
            
            if mcxhj == 'xhj':
            	res = Simsimi.simsimi(content)
            	resnum = res['status']
            	if resnum == 200:
                	reply_text = res['respSentence']
               	else:
                	reply_text = '小黄鸡脑袋出问题了，换个话题吧'
            	return self.render.reply_text(fromUser,toUser,int(time.time()),reply_text)   
            
            if type(content).__name__ == 'unicode':
            	content = content.encode('UTF-8')
            Nword = translation.youdao(content)
            return self.render.reply_text(fromUser,toUser,int(time.time()), Nword)	                 
        elif msgType == 'image':
        	pass       
    	elif msgType == 'event':
            content = xml.find("Event").text
            if content == 'subscribe':
                replayText = u'欢迎关注本微信'
                return self.render.reply_text(fromUser,toUser,int(time.time()), replayText)			
            elif content == 'unsubscribe':
                replayText = u'再见'
                return self.render.reply_text(fromUser,toUser,int(time.time()), replayText)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            