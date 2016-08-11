# -*- coding: utf-8 -*-
import gc


# 实现一个双链表的数据结构，同java中的LinkedList
# 链表的节点
class Node:
    def __init__(self, data, prev, next):
        self.next = next
        self.prev = prev
        self.data = data

    def show(self):
        print(self.data)


class LinkList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        return "first : %s  ;  last : %s  ;  size : %s " % (self.first.data, self.last.data, self.size)

    # 遍历链表
    def show(self):
        current = self.first
        while current is not None:
            print current.data,
            current = current.next

    # 是否为空
    def is_empty(self):
        return True if self.first is None else False

    # 插入到最后
    def insert(self, data):
        self._insert_to_last(data=data)
        return True

    # 同上,链表结构默认就是插入到最后一个位置
    def insert_last(self, data):
        self._insert_to_last(data=data)
        return True

    # 插入到第一个位置
    def insert_first(self, data):
        self._insert_to_first(data=data)
        return True

    # 插入一个数组
    def insert_all(self, data, index=0):
        self._check_position(index)
        self._insert_all(data, index)

    # 插入到某个角标的位置
    def insert_to_index(self, data, index):
        self._check_position(index)
        self._insert_before(data, index)
        return True

    # 清理
    def clear(self):
        current = self.first
        while current is not None:
            next = current.next
            current.data = None
            current.next = None
            current.prev = None
            current = next
        self.first = self.last = None
        self.size = 0
        gc.collect()

    # 判断包含某个值
    def contains(self, data):
        if self._index_of(data) == -1:
            return False
        return True

    # 判断是否包含某个数组
    def contains_all(self, data):
        for value in data:
            if self._index_of(value) == -1:
                return False
        return True

    # 获取first
    def get_first(self):
        return self.first

    # 获取last
    def get_last(self):
        return self.last

    # 根据坐标获取值
    def get(self, index):
        self._check_position(index)
        return self._node(index).data

    # 获取第一个值,但不删除他
    def peek_first(self):
        return self.first

    # 获取第一个值，并且删除他
    def poll_first(self):
        first, successor = self.first, None
        if self.first.next is not None:
            successor = self.first.next
        if successor is None:
            self.first = self.last = None
        else:
            self.first = successor
            successor.prev = None
        self.size -= 1
        return first

    # 获取最后一个值，但不删除他
    def peek_last(self):
        return self.last

    # 获取最后一个值，并且删除他
    def poll_last(self):
        pred, last = self.last.prev, self.last
        if last is self.first:
            self.first = self.last = None
        else:
            self.last = pred
            pred.next = None

        self.size -= 1
        return last

    # 删除头
    def remove_first(self):
        self._check_position(1)
        first, next = self.first, self.first.next
        if first is self.last:
            self.first = self.last = None
        else:
            self.first = next
            self.first.prev = None

        self.size -= 1
        return first

    # 删除尾
    def remove_last(self):
        self._check_position(1)
        last, pred = self.last, self.last.prev
        if last is self.first:
            self.first = self.last = None
        else:
            self.last = pred
            pred.next = None

        self.size -= 1
        return last

    # 检查某个角标是否合理
    def _check_position(self, index):
        if index > self.size or index < 0:
            raise Exception

    # 寻找某个角标的值
    def _node(self, index):
        result = None
        if index < self.size >> 1:
            result = self.first
            for i in range(1, index):
                result = result.next
        else:
            result = self.last
            for i in range(self.size, index, -1):
                result = result.prev
        return result

    # 插入到最后的实际执行方法
    def _insert_to_last(self, data):
        l = self.last  # 先获取最后一个元素
        new_node = Node(data, l, None)
        self.last = new_node

        if l is None:  # 如果最后节点为空，说明链表为空
            self.first = new_node
        else:
            l.next = new_node

        self.size += 1

    # 插入到第一个位置
    def _insert_to_first(self, data):
        f = self.first
        new_node = Node(data, None, f)
        self.first = new_node
        if f is None:
            self.last = new_node
        else:
            f.prev = new_node

        self.size += 1

    # 插到某个值的前面
    def _insert_before(self, data, index):
        before_node = self._node(index)
        temp_node = before_node.prev
        new_node = Node(data, temp_node, before_node)
        before_node.prev = new_node

        if temp_node is None:
            self.first = new_node
        else:
            temp_node.next = new_node

        self.size += 1

    # 从某个角标后开始插入一个数组
    def _insert_all(self, data, index):
        data_length = len(data)
        if data_length == 0:
            return False

        pred, successor = None, None
        if index == self.size:
            pred = self.last
        else:
            successor = self._node(index)
            pred = successor.prev
        for value in data:
            new_node = Node(value, pred, None)
            if pred is None:
                self.first = new_node
            else:
                pred.next = new_node
            pred = new_node

        if successor is None:
            self.last = pred
        else:
            pred.next = successor
            successor.prev = pred

        self.size += data_length
        return True

    # 定位某一个数据的坐标
    def _index_of(self, data):
        index = 1
        current = self.first
        while current is not None:
            if current.data == data:
                return index
            index += 1
            current = current.next
        return -1


if __name__ == "__main__":
    link_list = LinkList()
    l = list("love")
    link_list.insert_all(l)
