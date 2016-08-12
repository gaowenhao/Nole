# -*- coding: utf-8 -*-
import re
from adt.link_list import LinkList
from adt.tag import TagTree
from pquery_exception import IllegalExpression


# expression = "#div"
class Document(object):
    def __init__(self, document, expression=None):
        self.document = document
        self.parser(expression)

    def parser(self, expression):
        expression_rule = LinkList()  # 构造规则字典
        self._check_expression(expression)
        expression_link = LinkList()
        expression_link.insert_all(list(expression))

        while expression_link.size > 1:
            expression_rule.insert_last(self._get_expression(expression_link))

        tag_tree = TagTree(self.document)

    @staticmethod
    def _get_expression(expression_link, flag=0):
        first_symbol = expression_link.peek_first().data  # 把首符号弹出去号弹出去 如#div  .enable
        if not re.match('\w', first_symbol):
            expression_link.poll_first()
        if first_symbol == " " or first_symbol == ">":
            return ('less',)
        else:
            pass
        result = ""
        result_tuple = tuple()
        while expression_link.peek_first() is not None and not re.match(r'[\s|>|\[|\]]',
                                                                        expression_link.peek_first().data):
            result += expression_link.poll_first().data

        if first_symbol == "#":
            result_tuple = ('and', 'id', result)
        elif first_symbol == ".":
            result_tuple = ('and', 'class', result)
        elif re.match(r'\w.*', first_symbol):
            result_tuple = ('and', 'tag', result)
        elif first_symbol == "*":
            result_tuple = ('and', 'tag', '*')
        elif first_symbol == "[":
            expression_link.poll_first()  # 把最后一个中括号弹出
            array = result.split("=")
            result_tuple = ('and', array[0], array[1])

        return result_tuple

    # 检查表达式是否合法
    @staticmethod
    def _check_expression(expression):
        if not isinstance(expression, basestring):
            raise IllegalExpression
        if len(expression) < 2:
            raise IllegalExpression
        if not re.match(r"^[#|\w|\.|*].+", expression):
            raise IllegalExpression

