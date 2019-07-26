#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# History:
# 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true


import math
import time


class Solution:
    def isValid(self, sBrac):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dcBracket = {"{": "}", "(": ")", "[": "]"}
        lLeft = ["{", "(", "["]
        queue = []
        iLen = int(len(sBrac))
        if (iLen % 2 != 0):
            return False
        for iIndex in range(int(iLen)):
            cCur = sBrac[iIndex]
            if (cCur in lLeft):
                queue.append(cCur)
            else:
                if (0 == len(queue)):
                    return False
                cPop = queue.pop(-1)
                if (dcBracket[cPop] != cCur):
                    return False
        if (0 < len(queue)):
            return False
        return True


def main():
    # sInput = "([)]"
    sInput = "()[]{}"
    sInput = "(]"
    sInput = "{[]}"
    sInput = "(("

    solution = Solution()

    fStart = time.time()
    print(solution.isValid(sInput))
    fStop = time.time()
    print("time: ", (fStop - fStart) * 1000, "ms")
    # print(solution.judgePrime(4))


if __name__ == "__main__":
    main()
