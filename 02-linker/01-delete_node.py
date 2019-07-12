#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : delete_node.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# History:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    node = ListNode(4)
    node.next = ListNode(5)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(9)

    deleteNode(node.next)

    while(node != None):
        print(node.val)
        node = node.next
