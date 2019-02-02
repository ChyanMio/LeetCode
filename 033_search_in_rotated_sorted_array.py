# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:49:14 2019

@author: zhang
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]: l = mid + 1
            else: r = mid
                
        offset, l, r = l, 0, n - 1
        while l <= r:
            mid = (r + l) // 2
            n_mid = (mid + offset) % n
            if nums[n_mid] == target: return n_mid
            if nums[n_mid] < target: l = mid + 1
            else: r = mid - 1
        return -1