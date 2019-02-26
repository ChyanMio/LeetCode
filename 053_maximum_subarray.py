# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:34:37 2019

@author: zhang
"""

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        res, sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            sum = max(sum + nums[i], nums[i])
            res = max(res, sum)
        return res