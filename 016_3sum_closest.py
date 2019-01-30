# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:15:45 2019

@author: zhang
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if abs(val - target) < abs(res - target):
                    res = val
                if val < target:
                    j += 1
                elif val > target:
                    k -= 1
                else:
                    return target
        return res
        
        