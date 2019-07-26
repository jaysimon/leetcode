#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# History:o


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list2Tree(lList):
    lNodes = []
    for iNum in lList:
        nTmp = TreeNode(iNum)
        lNodes.append(nTmp)

    for iIndex in range(len(lNodes)):
        # print(nNode.val)
        if (iIndex * 2 + 2 > len(lNodes)):
            break
        if (lNodes[iIndex * 2 + 1].val):
            lNodes[iIndex].left = lNodes[iIndex * 2 + 1]
        else:
            lNodes[iIndex].left = None
        if (lNodes[iIndex * 2 + 2].val):
            lNodes[iIndex].right = lNodes[iIndex * 2 + 2]
        else:
            lNodes[iIndex].right = None
    return lNodes[0]


class Solution(object):
    def preTraverse(self, tRoot):
        if tRoot == None:
            return 0
        # print(tRoot.val)
        iLeft = self.preTraverse(tRoot.left)
        iRight = self.preTraverse(tRoot.right)
        iMax = iLeft if (iLeft > iRight) else iRight
        return iMax + 1

    def maxDepth(self, root):
        if root == None:
            return 0
        # print(root.val)
        iLeft = self.maxDepth(root.left)
        iRight = self.maxDepth(root.right)
        iMax = iLeft if (iLeft > iRight) else iRight
        return iMax + 1


if __name__ == "__main__":
    lList = [3, 9, 20, None, None, 15, 7]
    tRoot = list2Tree(lList)

    # preTraverse(tRoot)
    solution = Solution()

    print(solution.maxDepth(tRoot))
