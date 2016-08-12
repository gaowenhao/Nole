# -*- coding: utf-8 -*-
from core_selector import Document
from adt.link_list import LinkList
import sys
import urllib2
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False

    def handle_starttag(self, tag, attrs):
        if tag and tag == "div":
            if attrs:
                if attrs[0][0] == "class" and attrs[0][1] == "content":
                    self.flag = True
                    print "Encountered a start tag:", tag

    def handle_data(self, data):
        if self.flag:
            print "Encountered some data  :", data


if __name__ == "__main__":
    url = 'http://www.qiushibaike.com/hot/'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    document = response.read().decode('utf-8')

    parser = MyHTMLParser()
    parser.feed(document)

    # document = Document(document.decode('utf-8'), expression="#re[name=3]>cc[age=15]")
