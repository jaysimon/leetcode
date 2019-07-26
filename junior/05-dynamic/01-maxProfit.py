#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : maxProfit.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# History:

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (0 == len(prices)): return 0
        lPrices = prices
        iProfit = 0
        iMin = lPrices[0]

        for iIndex in range(len(lPrices)):
            iProfit = max(lPrices[iIndex] - iMin, iProfit)
            iMin = min(lPrices[iIndex], iMin)
        return iProfit


def main():
    lPrices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(lPrices))


if __name__ == "__main__":
    main()