# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:25:48 2019

@author: zhang
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, n = 0, len(height)
        i, j = 0, n - 1
        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]: i += 1
            else: j -= 1
        return res