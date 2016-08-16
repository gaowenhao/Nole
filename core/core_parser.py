# -*- coding: utf-8 -*-
import re
from adt.link_list import LinkList
from exception.exception import IllegalExpression
from collections import deque


# expression = "#div"  其实这个类都不应该存在。
class ExpressionParser(object):
    def __init__(self):
        pass

    @staticmethod
    def parser(expression):
        expression_rule = LinkList()  # 构造规则字典
        ExpressionParser._check_expression(expression)
        expression_link = LinkList()
        expression_link.insert_all(list(expression))

        while expression_link.size > 1:
            expression_rule.insert_last(ExpressionParser._get_expression(expression_link))

        return expression_rule

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
            result_tuple = ('id', result)
        elif first_symbol == ".":
            result_tuple = ('class', result)
        elif re.match(r'\w.*', first_symbol):
            result_tuple = ('tag', result)
        elif first_symbol == "*":
            result_tuple = ('tag', '*')
        elif first_symbol == "[":
            expression_link.poll_first()  # 把最后一个中括号弹出
            array = result.split("=")
            result_tuple = (array[0], array[1])

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


class BodyParser(object):
    def __init__(self, document):
        self.tree = deque([])
        self.document = BodyParser._getbody(document)
        BodyParser._build_tree(self.document)

    @staticmethod
    def _build_tree(body_array):
        print(body_array)

    @staticmethod
    def _getbody(document):
        body = re.search('<body(.|\s)*</body>', document).group()
        return deque(re.findall('<\w+[\w|\s|"|\'|=]*>', body))
