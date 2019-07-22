#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:
#
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# History:


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lNums = nums
        if (0 == len(lNums)):
            return 0
        if (1 == len(lNums)):
            return lNums[0]

        lMax = []
        lMax.append(lNums[0])
        lMax.append(lNums[1])
        if (0 == len(lNums)):
            return 0
        for iIndex in range(2, len(lNums)):
            iCur = lNums[iIndex]
            iMax = max(lMax[:-1]) + iCur
            lMax.append(iMax)
        return max(lMax)


def main():
    lNums = [2, 7, 9, 3, 1]
    lNums = [2, 1, 1, 2]
    # lNums = []
    lNums = [2, 1]
    solution = Solution()
    print(solution.rob(lNums))


if __name__ == "__main__":
    main()
