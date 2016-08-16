# -*- coding: utf-8 -*-
from collections import deque


class Tag(object):
    def __init__(self, tag, attribute, content, superior):
        self.tag = tag
        self.attribute = attribute  # 属性元组
        self.content = content  # 内容串
        self.superior = superior  # 上级tag对象
