#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 汉明距离
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 示例:
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。
# History:

import math
import time


class Solution(object):
    def hammingWeight(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """


def main():
    x = 1
    y = 4
    solution = Solution()

    fStart = time.time()
    print(solution.hammingWeight(x, y))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
