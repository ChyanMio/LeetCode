# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:42:07 2019

@author: zhang
"""

class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        res = ""
        c, i, j = 0, len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or c == 1:
            if i >= 0:
                c = c + ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                c = c + ord(b[j]) - ord('0')
                j -= 1
            res = str(c % 2) + res
            c = c // 2
            print(res, c)
        return res