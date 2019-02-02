# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:18:43 2019

@author: zhang
"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        def partition(nums):
            q = -1
            for i in range(0, len(nums)):
                if nums[i] > 0:
                    q += 1
                    nums[q], nums[i] = nums[i], nums[q]
            return q
        k = partition(nums) + 1 
        res = k + 1
        for i in range(k):
            tmp = abs(nums[i])
            if tmp <= k:
                nums[tmp - 1] = -nums[tmp - 1] if nums[tmp - 1] > 0 else nums[tmp - 1]
        for i in range(k):
            if nums[i] > 0:
                res = i + 1; break
        return res
    