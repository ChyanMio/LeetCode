# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:01:34 2019

@author: zhang
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #manacher algorithm, one application of dynamic programming
        s = '#' + '#'.join(s) + '#'
        dp = [0] * len(s)
        rightMax, pos = 0, 0
        maxLen, maxPos = 0, 0
        for i in range(len(s)):
            if i < rightMax:
                dp[i] = min(dp[2 * pos - i], rightMax - i)
            else:
                dp[i] = 1
            while i - dp[i] >= 0 and i + dp[i] < len(s) and s[i - dp[i]] == s[i + dp[i]]:
                dp[i] += 1
            if dp[i] + i - 1 > rightMax:
                rightMax, pos = dp[i] + i - 1, i
            if dp[i] > maxLen:
                maxLen, maxPos = max(maxLen, dp[i]), i
        t = s[maxPos - maxLen + 1 : maxPos + maxLen]
        return ''.join(t.split('#'))