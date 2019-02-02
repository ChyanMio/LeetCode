# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 19:23:05 2019

@author: zhang
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l