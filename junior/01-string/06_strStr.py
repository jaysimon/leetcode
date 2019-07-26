#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description: 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出
#   needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
# History:


def strStr(haystack:str, needle: str) -> int:
    return haystack.find(needle)



if __name__ == "__main__":
    print("%i, 2" % (strStr(haystack="hello", needle="ll")))
    print("%i, -1" % (strStr(haystack="aaaaa", needle="bba")))
    print("%i, 0" % (strStr(haystack="aaaaa", needle="")))