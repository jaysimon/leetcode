#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 三数之和
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# History:


import math
import time


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lNums = nums
        lNums.sort()
        iIndex = 1
        iLen = len(lNums)
        llResult = []

        print(lNums)
        if (0 < lNums[0] or 0 > lNums[-1]):
            return []
        while (iIndex < iLen - 1):
            iA = lNums[iIndex]
            # if (lNums[iIndex] == lNums[iIndex + 1]):
            #     iIndex += 1
            #     continue
            for jIndex in range(iIndex, -1, -1):
                iB = lNums[jIndex]
                if (lNums[jIndex] == lNums[jIndex + 1]):
                    continue
                for kIndex in range(iIndex + 1, len(lNums)):
                    iC = lNums[kIndex]

                    if (0 == iA + iB + iC):
                        llResult.append([iA, iB, iC])
            iIndex += 1
        return llResult


def main():
    lNums = [-1, 0, 1, 2, -1, -4]
    lNums = [-4, -1, -1, 0, 1, 2]
    # lNums = [0, 0, 0]
    solution = Solution()

    fStart = time.time()
    print(solution.threeSum(lNums))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))
    # print(list(range(1, -1, -1)))


if __name__ == "__main__":
    main()
