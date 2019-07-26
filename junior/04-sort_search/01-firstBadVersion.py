#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : firstBadVersion.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:第一个错误的版本
# History:


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    lVersions = [False, False, False, True, True]
    return lVersions[version]


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        iStart = 0
        iStop = n
        while (iStart+1 != iStop):
            if (isBadVersion(int((iStart + iStop) / 2))):
                iStart = iStart
                iStop = int((iStart + iStop) / 2)
            else:
                iStart = int((iStart + iStop) / 2)
                iStop = iStop
            # print("start", iStart)
            # print("stop", iStop)
            #
            # print("\n")
        print(iStop)
        return iStop

def main():
    lVersions = [False, False, False, True, True]

    solution = Solution()
    print(solution.firstBadVersion(5))


if __name__ == "__main__":
    main()
