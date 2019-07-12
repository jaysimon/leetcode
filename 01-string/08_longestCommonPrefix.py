#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : 08_longestCommonPrefix.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: 编写一个函数来查找字符串数组中的最长公共前缀。
# History:


import time


def longestCommonPrefix(strs) -> str:
    # sResult = ""
    # if 0 == len(strs):
    #     return ""
    # if 1 == len(strs):
    #     return strs[0]
    # iLen = len(strs)
    # sFir = strs[0]
    #
    # for jIndex in range(len(sFir)):
    #     cTmp = sFir[jIndex]
    #     for iIndex in range(1, iLen):
    #         if(jIndex >= len(strs[iIndex]) or strs[iIndex][jIndex] != cTmp):
    #             return sResult
    #     # print(cTmp, "\n")
    #     sResult += cTmp
    # return sResult
    if len(strs) == 0:    return ""
    if len(strs) == 1:    return strs[0]
    strs.sort()
    p = ""
    for x, y in zip(strs[0], strs[-1]):
        if x == y:
            p += x
        else:
            break
    return p

if __name__ == "__main__":
    sList = ["flower","flow","flightda"]
    print("fl ", longestCommonPrefix(sList))
    #
    # sList = ["dog","racecar","car"]
    # print("", longestCommonPrefix(sList))
    #
    # sList = ["aa","a"]
    # print("", longestCommonPrefix(sList))

    # sList = [""]
    # print("", longestCommonPrefix(sList))
    #
    # sList = ["", ""]
    # print("", longestCommonPrefix(sList))