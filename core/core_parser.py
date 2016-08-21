# -*- coding: utf-8 -*-
import re
from adt.link_list import LinkList
from exception.exception import IllegalExpression
from lxml import etree


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


def getResult(body,expressions):
    xpath = "//"

    for expression in iter(expressions):
        if expression.data[0] == "tag":
            xpath += expression.data[1]
        elif expression.data[0] == "less":
            xpath += "//"
        else:
            if xpath.endswith("/"):
                xpath += "*"
            xpath += '[@%s="%s"]' % (expression.data)
    temp_result = []
    page = etree.HTML(body)
    result = page.xpath(xpath)
    for val in result:
        for text in val.itertext():
            temp_result.append(text + "\n")
    return temp_result


def _clear_tag(tag):
    for subtag in list(tag):
        tag.remove(subtag)
    return tag