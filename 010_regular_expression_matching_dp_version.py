# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:05:18 2019

@author: zhang
"""
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-2] or (i > 0 and s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j]
                else:
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return dp[m][n]
