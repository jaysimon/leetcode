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
    if (not head):
        return None
    nCurrent = head
    nHead = ListNode(0)
    nHead.next = nCurrent
    while (nCurrent.next):
        # print(nCurrent.val, nCurrent.next.val)
        nNext = nCurrent.next

        nCurrent.next = nNext.next
        nNext.next = nHead.next
        nHead.next = nNext

        # new_node = nHead
        # while (new_node != None):
        #     print(new_node.val)
        #     new_node = new_node.next
        # print("\n")
    return nHead.next


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    new_node = node
    new_node = reverseList(node)

    while (new_node != None):
        print(new_node.val)
        new_node = new_node.next
