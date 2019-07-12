#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : reverseList.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# History:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    # iLen = 0
    # lNodes = []
    # tmp = ListNode(0)
    # if head == None:
    #     return None
    # while (head != None):
    #     lNodes.append(head)
    #     iLen += 1
    #     head = head.next
    #
    # for iIndex in range(iLen - 1):
    #     lNodes[-iIndex - 1].next = lNodes[-iIndex - 2]
    #
    # lNodes[0].next = None
    # return lNodes[-1]

    node = head
    tail  = None
    if head == None:
        return None
    while(True):
        next_node = node.next
        node.next = tail
        tail = node
        if next_node == None:
            break
        node = next_node
    return node



if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    new_node = reverseList(node)
    while (new_node != None):
        print(new_node.val)
        new_node = new_node.next
