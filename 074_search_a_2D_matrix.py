# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:16:34 2019

@author: zhang
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None: return False
        m, n = len(matrix), len(matrix[0])
        l, h = 0, m * n - 1
        while l <= h:
            mid = (l + h) // 2
            num = matrix[mid // n][mid % n]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                h = mid - 1
        return False