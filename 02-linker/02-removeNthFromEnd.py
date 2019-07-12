#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# History:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n:int) -> ListNode:
    iLen = 0
    tmp = head
    while(tmp != None):
        iLen += 1
        tmp = tmp.next

    if n == iLen:
        if head.next == None:
            return None
        else:
            return head.next

    iCount = 0
    tmp = head
    while(tmp != None):
        if iCount == iLen - n - 1:
            tmp.next = tmp.next.next
        # print(head.val)
        tmp = tmp.next
        iCount += 1
    return head


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    new_node = removeNthFromEnd(node, 2)

    while(new_node != None):
        print(new_node.val)
        new_node = new_node.next

    # node = ListNode(1)
    # new_node = removeNthFromEnd(node, 1)
    #
    # while (new_node != None):
    #     print(new_node.val)
    #     new_node = new_node.next