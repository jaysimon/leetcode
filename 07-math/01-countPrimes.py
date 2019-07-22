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


class Solution(object):
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
        lList = list(n)
        for iIndex in range(2, n):
            for jIndex in range(2, n):
                if()
        print(lList)
        return len(lList)


def main():
    solution = Solution()
    print(solution.countPrimes(1111113))
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
