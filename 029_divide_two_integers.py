# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:28:24 2019

@author: zhang
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n1, n2 = dividend, divisor
        if not n1: return 0
        flag = 1
        if n1 < 0:
            flag = -flag
            n1 = -n1
        if n2 < 0:
            flag = -flag
            n2 = -n2
        b, d = 1, n2
        e = d << 1
        while e <= n1:
            b = b << 1
            d = d << 1
            e = d << 1
        res = 0
        while b > 0:
            if n1 >= d:
                res += b
                n1 -= d
            b = b >> 1
            d = d >> 1
        if flag == -1:
            res = -res
        if res < -2147483648 or res > 2147483647:
            res = 2147483647
        return res
            