# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:52:29 2019

@author: zhang
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0x80000000:
            return 0
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
            if res > 0x7fffffff:
                return 0
        return res
        
        