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


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nFast = head
        nSlow = head

        if ((not head) or not (head.next)):
            return False

        while (nSlow and nFast):
            if (not nFast.next):
                return False
            nFast = nFast.next.next
            nSlow = nSlow.next
            if (nFast == nSlow):
                return True
        return False


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    nodes = None
    nodes = node1
    nodes.next = node2
    nodes.next.next = node3
    nodes.next.next.next = node4
    nodes.next.next.next.next = node2

    solution = Solution()

    print(solution.hasCycle(nodes))
