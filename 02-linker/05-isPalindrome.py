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

def reverseList(head: ListNode) -> ListNode:
    if (not head):
        return None
    nCurrent = head
    nHead = ListNode(0)
    nHead.next = nCurrent
    while (nCurrent.next):
        nNext = nCurrent.next

        nCurrent.next = nNext.next
        nNext.next = nHead.next
        nHead.next = nNext
    return nHead.next

def isPalindrome(head: ListNode) ->  bool:
    nHead = head
    nFast = head
    nSlow = head

    if((not nHead) or not (nHead.next)):
        return True

    while(nFast):
        if(not nFast.next):
            break
        nFast = nFast.next.next
        nSlow = nSlow.next

    nLast = reverseList(nSlow)

    # print("left:\n")
    # new_node = nHead
    # while (new_node != None):
    #     print(new_node.val)
    #     new_node = new_node.next
    # print("\n")
    #
    # print("right:\n")
    # new_node = nLast
    # while (new_node != None):
    #     print(new_node.val)
    #     new_node = new_node.next

    while(nLast and nHead):
        if(nHead.val != nLast.val):
            return False
        nHead = nHead.next
        nLast = nLast.next
    return True

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(1)
    # l1 = None
    print(isPalindrome(l1))