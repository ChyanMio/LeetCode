# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:48:11 2019

@author: zhang
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        cnt, n = 0, len(nums)
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1] and nums[i] == nums[i + 1]: cnt += 1
            else: nums[i - cnt] = nums[i]
        nums[n - 1 - cnt] = nums[n - 1]
        return n - cnt