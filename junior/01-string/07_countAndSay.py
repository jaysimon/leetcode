#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: Count and say
# History:


import time



def countAndSay(n: int) -> str:
    sStart = "1"
    n = n - 1
    for iIndex in range(n):
        jIndex = 0
        sTmp = ""

        while(jIndex < len(sStart)):
            kIndex = jIndex
            iCount = 0
            while(kIndex < len(sStart)):
                if(sStart[kIndex] != sStart[jIndex]):
                    break
                kIndex += 1
                iCount += 1
            sTmp += str(iCount)
            sTmp += sStart[jIndex]
            jIndex += iCount
        sStart = sTmp
        # print(sStart)
    return sStart
    # if n == 1: return '1'  # 递归出口
    # s = countAndSay(n - 1)
    # res, count = '', 0
    # for i in range(len(s)):
    #     count += 1
    #     if i == len(s) - 1 or s[i] != s[i + 1]:  # 最后一个字符串要提前终止
    #         res += str(count)
    #         res += s[i]
    #         count = 0
    # return res


if __name__ == "__main__":
    # print(countAndSay(1), 1)
    # print(countAndSay(4), "1211")

    time_start = time.time()
    print(countAndSay(30), "111221")
    time_end = time.time()
    print('totally cost: %.2f ms\n' % ((time_end - time_start)*1000))
