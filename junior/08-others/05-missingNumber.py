#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 缺失数字
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
# 示例 1:
#
# 输入: [3,0,1]
# 输出: 2
# 示例 2:
#
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
# History:

import math
import time


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lNums = nums
        iSum = 0
        iIndexSum = 0
        for iIndex in range(len(lNums)):
            iSum ^= lNums[iIndex] ^ (iIndex + 1)
        print(iSum)
        return iSum


def main():
    lNums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    # lNums = [3, 0, 1, 2, 4, 6]
    # lNums = [0, 1, 3]
    # lNums = [1,0]

    solution = Solution()

    fStart = time.time()
    print(solution.missingNumber(lNums))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
