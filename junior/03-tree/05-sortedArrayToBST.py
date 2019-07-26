#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : 04-levelOrder.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: 将有序数组转换为二叉搜索树
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

def levelTraverse(root):
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

class Solution:
    def add2tree(self, tRoot, lNums):
        iLen = len(lNums)
        if 0 == iLen:
            return None
        # tRoot.left = TreeNode(lNums[int(iLen / 4)])
        # tRoot.right = TreeNode(lNums[int(iLen * 3 / 4)])
        tRoot = TreeNode(lNums[int(iLen / 2)])
        # print("tRoot", tRoot.val)

        # if 1 == iLen:
        #     return tRoot
        lLeft = lNums[0:int(iLen / 2)]
        lRight = lNums[int(iLen / 2):]
        print(tRoot.val)
        print("left", lLeft)
        print("right", lRight)
        print("\n")
        tRoot.left = self.add2tree(tRoot.left, lNums[0:int(iLen / 2)])
        tRoot.right = self.add2tree(tRoot.right, lNums[int(iLen / 2)+1:])
        return tRoot

    def sortedArrayToBST(self, nums):
        lNums = nums
        iLen = int(len(lNums) / 2)
        tRoot = None
        tRoot = self.add2tree(tRoot, lNums)
        return tRoot
        print("finish")


if __name__ == "__main__":
    lList = [-10, -3, 0, 5, 9]
    # lList = [1,2,3,4,5,6,7]

    # tRoot = list2Tree(lList)

    solution = Solution()
    tRoot = solution.sortedArrayToBST(lList)
    print("----------")
    print(levelTraverse(tRoot))