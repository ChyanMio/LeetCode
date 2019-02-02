# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 23:07:21 2019

@author: zhang
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if not n or nums[n - 1] < target: return n
        if nums[0] > target: return 0
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target: l = mid + 1
            else: r = mid
        return r