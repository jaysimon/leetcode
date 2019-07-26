#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : climbStairs.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# History:


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归的时间太长
        # if (1 == n):
        #     return 1
        # if (2 == n):
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        if (1 == n or 2 == n):
            return n
        iPre2 = 1
        iPre1 = 2
        for iIndex in range(n-2):
            iTmp = iPre1
            iPre1 = iPre2 + iPre1
            iPre2 = iTmp
        return iPre1


def main():
    solution = Solution()
    print(solution.climbStairs(35))


if __name__ == "__main__":
    main()
