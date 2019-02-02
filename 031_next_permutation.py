# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:56:53 2019

@author: zhang
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]: break
            i -= 1
        if i < 0:
            self.reverse(nums, 0, n - 1)
            return
        j = n - 1
        while j > i:
            if nums[j] > nums[i]: break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1, n - 1)
        
    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1