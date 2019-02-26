# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:18:36 2019

@author: zhang
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        #类似斐波拉契
        f1, f2 = 0, 1
        n = len(s)
        s = [eval(i) for i in s]
        for i in range(n):
            f3 = 0
            if s[i] > 0: f3 += f2
            if i > 0 and s[i - 1] != 0 and s[i - 1] * 10 + s[i] <= 26:
                f3 += f1
            f1, f2 = f2, f3
        return f3