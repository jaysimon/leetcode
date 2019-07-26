#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : isValidBST.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: 验证二叉搜索树
# History:


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


class Solution(object):
    nPre = None
    def midTraverse(self, tRoot):
        if tRoot == None:
            return 0
        # print(tRoot.val)
        iLeft = self.midTraverse(tRoot.left)
        print(tRoot.val)
        self.lNums.append(tRoot.val)
        iRight = self.midTraverse(tRoot.right)
        return 0

    def isValidBST(self, root):
        # if(None == root):
        #     return True
        # self.midTraverse(root)
        # for iIndex in range(len(self.lNums) - 1):
        #     if(self.lNums[iIndex] >= self.lNums[iIndex + 1]):
        #         return False
        # return True.
        tRoot = root
        if(None == tRoot):
            return True
        nPre = tRoot
        self.isValidBST(tRoot.left)
        self.isValidBST(tRoot.right)




if __name__ == "__main__":
    lList = [3, 9, 20, None, None, 15, 7]
    # lList = [2, 1, 3]
    # lList = [5, 1, 6, None, None, 3, 7]
    # lList = [10, 5, 15, None, None, 6, 20]
    lList = [1, 1]
    tRoot = list2Tree(lList)

    # preTraverse(tRoot)
    solution = Solution()

    print(solution.isValidBST(tRoot))
