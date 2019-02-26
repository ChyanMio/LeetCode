# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:30:05 2019

@author: zhang
"""

class Solution:
    """
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
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        if m == 0 or n == 0: return 0
        a = [0 for _ in range(m)]
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    a[j] = 0
                else:
                    a[j] += 1
            res = max(res, self.largestRectangleArea(a))
        return res
    """
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans