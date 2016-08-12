# -*- coding: utf-8 -*-
from core_selector import Document
from adt.link_list import LinkList
import sys
import urllib2

if __name__ == "__main__":
    url = 'http://www.qiushibaike.com/hot/'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    document = response.read();
    document = Document(document.decode('utf-8'), expression="#re[name=3]>cc[age=15]")
