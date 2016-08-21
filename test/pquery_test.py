# -*- coding: utf-8 -*-
import urllib2
from HTMLParser import HTMLParser

from core.core_parser import *

if __name__ == "__main__":
    expression_rule = ExpressionParser.parser("#content #content-left .content")

    url = 'http://www.qiushibaike.com/hot/'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    document = response.read().decode('utf-8')
    result = getResult(document, expression_rule)

    for val in result:
        print(val)
