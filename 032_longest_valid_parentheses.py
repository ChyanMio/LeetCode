# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:20:33 2019

@author: zhang
"""

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls, res = len(s), 0
        stack = [-1]
        for i in range(ls):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not(len(stack)):
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res