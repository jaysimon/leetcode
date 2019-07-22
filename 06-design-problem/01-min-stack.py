#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : demo.py
# Author : Hou Wei
# Version : V1.0
# Date: 2019-02-21
# Description:
# 最小栈
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2
# History:

class MinStack(object):
    """min()为python内置方法，时间复杂度为O(n),所以一定要利用栈的特性，想别的方法。
        算法：
        1.首先在此方法中构造出两个以顺序表为形式的栈，一个用于正常情况，另一个在各种操作的时候记住最小值，这样就可以回避遍历的算法
        2.压栈，最小栈小的在上，大的在下，如果进来的比顶端的值大，则不压栈
        3.出栈，如果两个栈的顶端的值 都是相同的，则出栈
        4.顶端值正常，最小方法，直接输出顶端值即可
        tips：
        1.注意list[-1]，以及list.pop()，一定要排除空的情况
        2.注意list.pop()的操作会影响list，一定要注意步骤
        2.注意如果进来了相同的值，也要压栈。所以在压栈方法中，是大于等于而不是大于
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lList = []
        self.lMin = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.lList.append(x)
        if (0 == len(self.lMin)):
            self.lMin.append(x)
        elif (self.lMin[-1] >= x):
            self.lMin.append(x)

    def pop(self):
        """
        :rtype: None
        """
        iPop = self.lList[-1]
        if (iPop == self.lMin[-1]):
            self.lMin.pop(-1)
        return self.lList.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.lList[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.lMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def main():
    minStack = MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())


if __name__ == "__main__":
    main()
