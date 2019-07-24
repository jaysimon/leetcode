#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : isPowerOfThree.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 3的幂
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1:
#
# 输入: 27
# 输出: true
# 示例 2:
#
# 输入: 0
# 输出: false
# 示例 3:
#
# 输入: 9
# 输出: true
# 示例 4:
#
# 输入: 45
# 输出: false
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# History:


import math
import time


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (0 >= n):
            return False
        # 无循环解法
        # fLog = math.log(n, 3)
        # print(fLog)
        # if (abs(fLog - round(fLog)) < 0.000000001):
        #     return True
        # return False

        # 有循环解法
        while (n > 1):
            if (0 == n % 3):
                n = n/3
            else:
                return False
        if(1==n):
            return True

def main():
    solution = Solution()

    fStart = time.time()
    print(solution.isPowerOfThree(242))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
