# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:09:39 2019

@author: zhang
"""

class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1): dp[i][1] = dp[i - 1][1] + grid[i - 1][0]
        for j in range(1, n + 1): dp[1][j] = dp[1][j - 1] + grid[0][j - 1]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]