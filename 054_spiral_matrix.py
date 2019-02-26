# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:01:35 2019

@author: zhang
"""

class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        res = []
        if not matrix: return res
        rl, rr, cl, cr = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while rl <= rr and cl <= cr:
            for i in range(cl, cr + 1):
                res.append(matrix[rl][i])
            rl += 1
            for i in range(rl, rr + 1):
                res.append(matrix[i][cr])
            cr -= 1
            if rl <= rr:
                for i in range(cr, cl - 1, -1):
                    res.append(matrix[rr][i])
            rr -= 1
            if cl <= cr:
                for i in range(rr, rl - 1, -1):
                    res.append(matrix[i][cl])
            cl += 1
        return res
        #return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])