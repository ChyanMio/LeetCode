# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 19:22:06 2019

@author: zhang
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt,n = 0, len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
        return n - cnt