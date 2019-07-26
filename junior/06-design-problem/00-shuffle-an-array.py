#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:Shuffle an Array
# 打乱一个没有重复元素的数组。
#
# 示例:
#
# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();
#
# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();
#
# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();
# History:

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lNums = nums
        self.lPreserve = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.lPreserve

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.lNums)
        return self.lNums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

def main():
    nums = [1, 2, 3]
    # lNums = []
    # lNums = [1]
    solution = Solution(nums)
    print(solution.shuffle())
    print(solution.reset())
    print(solution.shuffle())


if __name__ == "__main__":
    main()
