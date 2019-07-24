#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : romanToInt.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 帕斯卡三角形
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# History:


import math
import time


class Solution:
    def reverseBits(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lResult = []
        llResult = []
        if (1 == n):
            return [1]
        lTmp = [1]
        for iIndex in range(n):
            for jIndex in range(iIndex + 1):
                # print(iIndex, jIndex)
                if (0 == jIndex):
                    lResult.append(1)
                elif(iIndex == jIndex):
                    lResult.append(1)
                    break
                else:
                    lResult.append(lTmp[jIndex] + lTmp[jIndex + 1])
                print(lResult)
                lTmp = lResult.copy()
                lResult = []
            llResult.append(lResult)
            print("---")
            # print(llResult)
        # print(llResult)


def main():
    iN = 5

    solution = Solution()

    fStart = time.time()
    print(solution.reverseBits(iN))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
