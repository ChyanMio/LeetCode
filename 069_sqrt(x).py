# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:59:19 2019

@author: zhang
"""

class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        #Newton
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r