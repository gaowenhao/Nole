# -*- coding: utf-8 -*-
import urllib2
from HTMLParser import HTMLParser

from core.core_parser import ExpressionParser
from core.core_parser import BodyParser


class MyHTMLParser(HTMLParser):
    def __init__(self, expression_rule):
        self.current_result = None
        self.flag = False

    def _has_attr(attrs, require_attr):
        for tup in attrs:
            if tup and tup[0] == require_attr[0] and tup[1] == require_attr[1]:
                return True
        return False

    def handle_starttag(self, tag, attrs):
        self.current_result = MyHTMLParser._build_start_tag(tag, attrs)
        if expression_rule[1] == "tag":
            if tag == expression_rule[3]:
                self.flag = True
        elif expression_rule[0] != "less":
                self.flag = True

    def handle_endtag(self, tag):
        if tag == expression_rule[3]:
            self.current_result += "</"+expression_rule[3]+">"
            self.flag = False

    def handle_data(self, data):
        if self.flag:
            self.current_result += data

    @staticmethod
    def _build_start_tag(tag, attrs):
        result = '<' + tag + " "
        for attr in attrs:
            result += attr[0] + "=" + attr[1] + " "
        result += ">"
        return result

    def get_result(self):
        return self.current_result

if __name__ == "__main__":
    expression_rule = ExpressionParser.parser("#div root[name=3]")

    url = 'http://www.qiushibaike.com/hot/'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    document = response.read().decode('utf-8')

    b = BodyParser(document)

    expression_rule.show()


