# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:02:03 2019

@author: zhang
"""

class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        i, n = 0, len(nums)
        reach = 0
        while i < n and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1
        return i == n