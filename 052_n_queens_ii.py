# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 00:25:53 2019

@author: zhang
"""

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        def dfs(queens, dif, sum):
            p = len(queens)
            if p == n: 
                self.res += 1
                return None
            for q in range(n):
                if q not in queens and p - q not in dif and p + q not in sum:
                    dfs(queens + [q], dif + [p - q], sum + [p + q])
        dfs([], [], [])
        return self.res