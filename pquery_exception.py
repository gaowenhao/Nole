# -*- coding: utf-8 -*-
"""表达式异常"""


class IllegalExpression(Exception):
    def __init__(self, val="Your expression is Illegal!"):
        self.val = val

    def __str__(self):
        return repr(self.val)
