# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:03:29 2019

@author: zhang
"""

class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        #mathematical solution
        s = [str(i) for i in range(1, n + 1)]
        fac = 1
        for i in range(1, n): fac *= i
        res = ""
        while k > 0 and k <= fac*n:
            g = k // fac
            k %= fac
            if k > 0:
                tmp = s.pop(g)
                res += tmp
            else:
                tmp = s.pop(g - 1)
                res += tmp
                s.reverse()
                add = "".join(s)
                res += add
                break
            fac = fac // len(s)
        return res