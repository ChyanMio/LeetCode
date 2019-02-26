# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:29:01 2019

@author: zhang
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res