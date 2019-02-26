# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:00:10 2019

@author: zhang
"""

class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        a, b, c = 1, 1, 1
        for i in range(n - 1):
            c = a + b
            a, b = b, c
        return c