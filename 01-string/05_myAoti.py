#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : my_aoti.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: Convert string to int
# History:

def my_aoti(str):
    iResult = 0
    sList = []
    str = str.strip()
    if (len(str) == 0):
        return 0
    cFirst = str[0]
    if (not ((ord(cFirst) >= 48 and ord(cFirst) <= 57) or
             cFirst == "-" or cFirst == "+")):
        return 0
    else:
        if(cFirst != "-" and cFirst != "+"):
            iIndex = 0
        else:
            iIndex = 1
        while(iIndex < len(str) and
                ord(str[iIndex]) >= 48 and ord(str[iIndex]) <= 57):
            sList.append(str[iIndex])
            iIndex += 1
        for jIndex in range(len(sList)):
            iResult += (ord(sList[-jIndex-1]) - 48) * pow(10, jIndex)
        if(cFirst == "-"):
            iResult = -iResult

    if iResult < -2147483648:
        iResult = -2147483648
    elif(iResult > 2147483647):
        iResult = 2147483647
    return iResult

if __name__ == "__main__":
    print("input:42, output:%s , expected output: 42 " % (str(my_aoti("42"))))
    print("input:  -42, output:%s , expected output: -42 " %
        (str(my_aoti("   -42"))))
    print("input:4193 with words, output:%s , expected output: 4193 " %
        (str(my_aoti("4193 with words"))))
    print("input:words and 987, output:%s , expected output: 0 " %
        (str(my_aoti("words and 987"))))
    print("input:-91283472332, output:%s , expected output: -2147483648 " %
        (str(my_aoti("-91283472332"))))
    print("input:, output:%s , expected output:0" %
        (str(my_aoti(""))))
    print("input: +1, output:%s , expected output:1" %
        (str(my_aoti("+1"))))
