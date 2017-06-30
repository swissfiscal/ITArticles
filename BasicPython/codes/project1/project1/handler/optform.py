#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 Created on  2017-06-30.
 @author: lwb
 desc:
'''
#!/usr/bin/env python
#coding:utf-8
import tornado.web
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class OptionForm(tornado.web.RequestHandler):
    def post(self):
        website = self.get_argument("website")      #接收名称为'website'的表单内容
        self.render("info.html",web=website)