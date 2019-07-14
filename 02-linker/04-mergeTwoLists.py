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
    nodeA = l1
    nodeB = l2
    nodeHead = ListNode(0)

    if (not nodeA):
        return nodeB
    if (not nodeB):
        return nodeA

    nodeResult = nodeHead
    while (nodeA and nodeB):
        if (nodeA.val < nodeB.val):
            nodeHead.next = nodeA
            nodeA = nodeA.next
        else:
            nodeHead.next = nodeB
            nodeB = nodeB.next
        nodeHead = nodeHead.next
        # nodeNew = nodeResult
        # while (nodeNew != None):
        #     print(nodeNew.val)
        #     nodeNew = nodeNew.next

    if(nodeA):
        nodeHead.next = nodeA
    else:
        nodeHead.next = nodeB

    return nodeResult.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    # l2 = None
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    nodeNew = mergetTwoLists(l1, l2)


    while (nodeNew != None):
        print(nodeNew.val)
        nodeNew = nodeNew.next
