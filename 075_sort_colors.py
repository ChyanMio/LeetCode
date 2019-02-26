# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:30:54 2019

@author: zhang
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #fucking boring problem
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        while i <= j:
            if nums[i] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            elif nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
                j = min(j, k)
            else:
                i += 1