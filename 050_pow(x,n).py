# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:59:27 2019

@author: zhang
"""

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0.0 or x == 1.0: return x
        if n == 0: return 1.0
        if n == -2147483648:
            y = self.myPow(x, n // 2)
            return y * y
        if n < 0:
            return 1 / self.myPow(x, -n)
        y = self.myPow(x, n // 2)
        res = y * y
        if n % 2 == 1: res *= x
        return res