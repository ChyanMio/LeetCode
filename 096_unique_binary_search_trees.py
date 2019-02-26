# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:54:30 2019

@author: zhang
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for root in range(2, n + 1):
            for child in range(1, root + 1):
                dp[root] += dp[root - child] * dp[child - 1]
        return dp[n]