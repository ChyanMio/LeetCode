# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:33:10 2019

@author: zhang
"""

class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        res = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            d = digits[i] + carry
            if d > 9:
                d = 0
                carry = 1
            else: carry = 0
            res.append(d)
        if carry > 0: res.append(carry)
        res.reverse()
        return res