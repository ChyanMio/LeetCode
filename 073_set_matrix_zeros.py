# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:15:58 2019

@author: zhang
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        if n == 0 or m == 0: return 
        r0, c0 = False, False
        for i in range(n):
            if matrix[i][0] == 0:
                c0 = True
        for j in range(m):
            if matrix[0][j] == 0:
                r0 = True
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, n):
            if matrix[i][0] != 0:
                continue
            for j in range(m):
                matrix[i][j] = 0
        for j in range(1, m):
            if matrix[0][j] != 0:
                continue
            for i in range(n):
                matrix[i][j] = 0
        if r0:
            for j in range(m):
                matrix[0][j] = 0
        if c0:
            for i in range(n):
                matrix[i][0] = 0
        """
        points = [[i, j] for j in range(len(matrix[0])) for i in range(len(matrix)) if matrix[i][j] == 0]#using set may perform better
        for i, j in points:
            matrix[i] = [0] * len(matrix[0])
            for n in range(len(matrix)):
                matrix[n][j] = 0       