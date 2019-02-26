# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:27:28 2019

@author: zhang
"""

class Solution:
    def generateMatrix(self, n: 'int') -> 'List[List[int]]':
        res = [[0 for i in range(n)] for j in range(n)]
        rl, rr, cl, cr = 0, n - 1, 0, n - 1
        cnt = 1
        while rl <= rr and cl <= cr:
            for i in range(cl, cr + 1):
                res[rl][i] = cnt
                cnt += 1
            rl += 1
            for j in range(rl, rr + 1):
                res[j][cr] = cnt
                cnt += 1
            cr -= 1
            for k in range(cr, cl - 1, -1):
                res[rr][k] = cnt
                cnt += 1
            rr -= 1
            for l in range(rr, rl - 1, -1):
                res[l][cl] = cnt
                cnt += 1
            cl += 1
        return res