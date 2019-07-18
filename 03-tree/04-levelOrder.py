#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : 04-levelOrder.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: 按照层级遍历
# History:


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list2Tree(lList):
    if (0 == len(lList)):
        return None
    lNodes = []
    for iNum in lList:
        nTmp = TreeNode(iNum)
        lNodes.append(nTmp)

    for iIndex in range(len(lNodes)):
        # print(nNode.val)
        if (iIndex * 2 + 1 >= len(lNodes)):
            break
        if (lNodes[iIndex * 2 + 1].val):
            lNodes[iIndex].left = lNodes[iIndex * 2 + 1]
        else:
            lNodes[iIndex].left = None
        if (iIndex * 2 + 2 >= len(lNodes)):
            break
        if (lNodes[iIndex * 2 + 2].val):
            lNodes[iIndex].right = lNodes[iIndex * 2 + 2]
        else:
            lNodes[iIndex].right = None
    return lNodes[0]


class Solution:
    lList = []

    def levelTraverse(self, tRoot):
        lTmp = []
        if tRoot == None:
            return None

        queue = []

        queue.append(tRoot)
        while (queue):
            lTmp = []
            for iIndex in range(len(queue)):
                lTmp.append(queue[iIndex].val)
            lList.append(lTmp)
            current_node = queue.pop(0)

            print(current_node.val)

            if (current_node.left):
                queue.append(current_node.left)
            if (current_node.right):
                queue.append(current_node.right)
        print(lList)
        return 0


if __name__ == "__main__":
    lList = [1, 2, 3, 4, 5, 6, 7]
    # lList = [1, 2, 2, None, 3, None, 3]
    # lList = [1, 2, 2, 3, 4, 4, 3]
    # lList = [1, 2, 2]
    # lList = [1, 2, 2, 2, None, 2]

    tRoot = list2Tree(lList)
    solution = Solution()
    solution.levelTraverse(tRoot)
