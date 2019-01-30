# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:17:05 2019

@author: zhang
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y, r = x, 0
        while y > 0:
            r = r * 10 + y % 10
            y = y // 10
        return r == x