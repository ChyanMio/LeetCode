# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:10:45 2019

@author: zhang
"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n < 3:
            return res
        nums.sort()
        i = 0
        while i < n and nums[i] <= 0:
            j = i + 1
            k = n - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val < 0:
                    j += 1
                    continue
                if val > 0:
                    k -= 1
                    continue
                res.append([nums[i], nums[j], nums[k]])
                while j + 1 < k and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res
        