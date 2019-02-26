# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 13:25:03 2019

@author: zhang
"""

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queens, dif, sum):
            p = len(queens)
            if p == n: 
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in dif and p + q not in sum:
                    dfs(queens + [q], dif + [p - q], sum + [p + q])
        result = []
        dfs([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]