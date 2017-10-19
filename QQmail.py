#! /usr/bin/env python2.7
# -*- coding:utf-8-*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


# --------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2016.10.27 15:00
#     USAEG :
#     login login beijing
# --------------------------------------------------#

import requests
import sys
import os
import time
import base64
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


class QQMail(object):
    """docstring for QQMail"""

    def __init__(self, QQnum, password, url):
        self.QQnum = QQnum
        self.password = password
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                   'Accept-Encoding': 'gzip, deflate', 'Referer': url}
        Host = (url.split(':')[1][2:]).split('/')[0]
        self.url = url
        #headers['Host'] = Host
        self.headers = headers

    def Login(self):
        sess = requests.Session()
        url = 'https://mail.qq.com/cgi-bin/loginpage'
        req = sess.get(self.url, headers=self.headers)
        with open("QQMail.html", 'wb') as htmlWriter:
            htmlWriter.writelines(req.content)

if __name__ == '__main__':
    url = 'https://ui.ptlogin2.qq.com/cgi-bin/login?style=9&appid=522005705&daid=4&s_url=https%3A%2F%2Fw.mail.qq.com'
    QQnum = "295948589"
    password = "xxxxxxx"
    login = QQMail(QQnum, password, url)
    login.Login()
# https://ui.ptlogin2.qq.com/cgi-bin/login?style=9&appid=522005705&daid=4&s_url=https%3A%2F%2Fw.mail.qq.com

#https://ssl.ptlogin2.mail.qq.com/check_sig?pttype=1&uin=295948589&service=login&nodirect=0&ptsigx=cdaf2050fd5880083d71d6c693d5d8fd1ec9313dd053b391a5ef96ee7082ec652703a8216a40681cccd09071f8e09de78ab5644a5a66e598ae519d2c13d606c0&s_url=https%3A%2F%2Fmail.qq.com%2Fcgi-bin%2Flogin%3Fvt%3Dpassport%26vm%3Dwpt%26ft%3Dloginpage%26target%3D%26account%3D295948589&f_url=&ptlang=2052&ptredirect=101&aid=522005705&daid=4&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=1&pt_aid=0&pt_aaid=0&pt_light=0&pt_3rd_aid=0
