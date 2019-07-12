#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : 04-mergeTwoLists.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# History:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergetTwoLists(l1, l2):
    while(True):
        if(l1.val < l2.val):
            l1.next = l2
            tmp = l2
            l2.next = l1.next
        else:




if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    new_node = mergetTwoLists(l1, l2)
    while (new_node != None):
        print(new_node.val)
        new_node = new_node.next
