# -*- coding: utf-8 -*-
import re
from adt.link_data_struct import LinkList
from pquery_exception import IllegalExpression


# expression = "#div"
class Document:
    def __init__(self, document, expression=None):
        if expression is None:
            self.document = document
        else:
            self.parser(document, expression)

    def parser(self, document, expression):
        expression_rule = dict()  # 构造规则字典
        self._check_expression(expression)
        expression_link = LinkList()
        expression_link.insert_all(list(expression))
        if expression_link.peek_first().data == "#":
            expression_rule['id'] = self._get_expression_id(expression_link)
        pass

    @staticmethod
    def _get_expression_id(expression_link):
        expression_link.poll_first()  # 把#号弹出去
        result_array = []
        while expression_link.peek_first().data != " ":
            result_array.append(expression_link.poll_first().data)
        return "".join(result_array)

    # 检查表达式是否合法
    @staticmethod
    def _check_expression(expression):
        if not isinstance(expression, basestring):
            raise IllegalExpression
        if len(expression) < 2:
            raise IllegalExpression
        if not re.match(r"^[#|\d|\.|:|*].+", expression):
            raise IllegalExpression
