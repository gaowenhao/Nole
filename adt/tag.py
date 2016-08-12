# -*- coding: utf-8 -*-
import re
import HTMLParser
from adt.link_list import LinkList


class Tag(object):
    def __init__(self, tag_name, attribute, inferior):
        self.content = tag_name
        self.attribute = attribute
        self.inferior = inferior


class TagTree(object):
    def __init__(self, document):
        self._parser(document)
        self.root = None

    def _parser(self, document):
        body = re.search(r'<body(.|\s)*</body>', document)
        if body:
            self._build_tree(body.group())

    def _build_tree(self):
        pass


