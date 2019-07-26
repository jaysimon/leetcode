#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:计数质数
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# History:

import math
import time


class Solution(object):
    # 判断质数的办法
    # def judgePrime(self, iNum):
    #     for iIndex in range(2, int(math.sqrt(iNum)+1)):
    #         # print(iNum % iIndex)
    #         if (0 == iNum % iIndex):
    #             return False
    #     return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n < 2):
            return 0

        lList = [1] * n
        iSqrt = int(math.sqrt(n))
        lList[0] = 0
        lList[1] = 0

        for iIndex in range(2, iSqrt + 1):
            if (1 == lList[iIndex]):
                lList[iIndex * iIndex:n:iIndex] = [0] * len(
                    lList[iIndex * iIndex:n:iIndex])

        return sum(lList)


def main():
    solution = Solution()

    fStart = time.time()
    print(solution.countPrimes(10))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
