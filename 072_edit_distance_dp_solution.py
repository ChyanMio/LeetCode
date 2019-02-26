# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:08:43 2019

@author: zhang
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Levenshtein distance
        m = len(word1)
        n = len(word2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1): dp[i][0] = i;
        for j in range(1, n+1): dp[0][j] = j;
        for i in range(1, m+1):
            for j in range(1, n+1):
                cost = 0 if(word1[i-1] == word2[j-1]) else 1
                dp[i][j] = min(dp[i-1][j-1]+cost, min(dp[i-1][j]+1, dp[i][j-1]+1))
        return dp[m][n]