#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# History:


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lNums = nums
        if (0 == len(lNums)):
            return None
        iMax = lNums[0]
        iPre = lNums[0]
        for iIndex in range(1, len(lNums)):
            iPre = max(lNums[iIndex], iPre + lNums[iIndex])
            if(iPre > iMax):
                iMax = iPre
        return iMax


def main():
    lNums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # lNums = []
    lNums = [1]
    solution = Solution()
    print(solution.maxSubArray(lNums))


if __name__ == "__main__":
    main()
