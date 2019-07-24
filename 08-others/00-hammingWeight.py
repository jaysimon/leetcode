#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 位1的个数
# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
#
#
#
# 示例 1：
#
# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
# 示例 2：
#
# 输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
# 示例 3：
#
# 输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
#
#
# 提示：
#
# 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
#
#
# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？
# History:


import math
import time


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sN = str(bin(n))
        # iResult = 0
        # print(sN)
        # for iIndex in range(2, len(sN)):
        #     if (str(1) == sN[iIndex]):
        #         iResult += 1
        # return iResult

        iResult = 0
        while(n):
            iResult+=1
            n &= (n-1)
        return iResult


def main():
    n = 111541654185649
    solution = Solution()

    fStart = time.time()
    print(solution.hammingWeight(n))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
