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
    def levelTraverse(self, root):
        tRoot = root
        lResult = []
        if tRoot == None:
            return lResult

        queue = []

        queue.append(tRoot)
        while (queue):
            iLen = len(queue)
            lTmp = []
            nextQue = []
            for iIndex in range(iLen):
                tTmp = queue[iIndex]
                # if not tTmp:
                #     break
                lTmp.append(tTmp.val)
                if(tTmp.left):
                    nextQue.append(queue[iIndex].left)
                if(tTmp.right):
                    nextQue.append(queue[iIndex].right)
            queue = nextQue

            lResult.append(lTmp)
            print(lResult)
        return lResult


if __name__ == "__main__":
    lList = [1, 2, 3, None, 5, 6, 7]
    # lList = []
    # lList = [1, 2, 2, None, 3, None, 3]
    # lList = [1, 2, 2, 3, 4, 4, 3]
    # lList = [1, 2, 2]
    # lList = [1, 2, 2, 2, None, 2]
    lList = [3, 9, 20, None, None, 15, 7]

    tRoot = list2Tree(lList)
    solution = Solution()
    solution.levelTraverse(tRoot)
