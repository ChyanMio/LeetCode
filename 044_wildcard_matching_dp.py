# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:11:45 2019

@author: zhang
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #much slower and bigger
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(ls + 1)] for _ in range(lp + 1)]
        dp[0][0] = True
        for i in range(1, lp + 1):
            if p[i - 1] == '*' and dp[i - 1][0]: dp[i][0] = True
        for i in range(1, lp + 1):
            for j in range(1, ls + 1):
                if p[i - 1] == '*': dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else: dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '?')
        return dp[lp][ls]
        