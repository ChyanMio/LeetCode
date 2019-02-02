# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:36:38 2019

@author: zhang
"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #linear dp
        n = len(height)
        if n < 3: return 0
        dp = [0 for _ in range(n)]
        res, mx = 0, 0
        for i in range(n):
            dp[i] = mx
            mx = max(mx, height[i])
        mx = 0
        for i in range(n - 1, -1, -1):
            dp[i] = min(dp[i], mx)
            mx = max(mx, height[i])
            if dp[i] > height[i]: res += dp[i] - height[i]
        return res