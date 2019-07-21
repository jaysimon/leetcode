#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : merge.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1
#   中，使得 num1 成为一个有序数组。
# History:


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        # nums1[m:] = nums2
        # nums1.sort()
        iIndex = m - 1
        jIndex = n - 1
        kIndex = len(nums1) - 1

        while (iIndex >= 0 and jIndex >= 0):
            if (nums1[iIndex] > nums2[jIndex]):
                nums1[kIndex] = nums1[iIndex]
                kIndex -= 1
                iIndex -= 1
            else:
                nums1[kIndex] = nums2[jIndex]
                kIndex -= 1
                jIndex -= 1
            print(nums1)
        nums1[:jIndex + 1] = nums2[:jIndex + 1]


def main():
    # lNum1 = [1, 2, 3, 0, 0, 0]
    lNum1 = [0]
    # lNum2 = [2, 5, 6]
    lNum2 = [1]
    # lNum1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    # lNum2 = [1, 2, 3]

    iM = 0
    iN = 1

    solution = Solution()
    solution.merge(lNum1, iM, lNum2, iN)
    print(lNum1)
    # for iIndex in range(2):
    #     print(iIndex)


if __name__ == "__main__":
    main()
