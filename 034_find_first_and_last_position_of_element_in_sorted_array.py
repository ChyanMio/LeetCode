# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 23:00:34 2019

@author: zhang
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums: return res
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target: l = mid + 1
            else: r = mid
        if nums[l] != target: return res
        res[0], r = l, len(nums) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if nums[mid] > target: r = mid - 1
            else: l = mid
        res[1] = r
        return res