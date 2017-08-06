# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree

class Translation:
	def	youdao(word)
    qword = urllib2.quote(word)	#屏蔽特殊字符，为了得到规范url
    baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=yourAppName&key=yourAppKey&type=data&doctype=json&version=1.1&q='
    url = baseurl + qword
    
    