#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# Fizz Buzz
# 写一个程序，输出从 1 到 n 数字的字符串表示。
#
# 1. 如果 n 是3的倍数，输出“Fizz”；
#
# 2. 如果 n 是5的倍数，输出“Buzz”；
#
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
#
# 示例：
#
# n = 15,
#
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
# History:

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lResult = []
        for iIndex in range(1, n + 1):
            if(0 == iIndex % 3 and 0 == iIndex % 5):
                lResult.append("FizzBuzz")
            elif(0==iIndex%3):
                lResult.append("Fizz")
            elif(0==iIndex%5):
                lResult.append("Buzz")
            else:
                lResult.append(str(iIndex))
        return lResult


def main():
    solution = Solution()
    print(solution.fizzBuzz(15))


if __name__ == "__main__":
    main()
