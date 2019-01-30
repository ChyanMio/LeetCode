# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:46:59 2019

@author: zhang
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, n = [], len(nums)
        if n < 4: return res
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target: continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target: continue
                k, l = j + 1, n - 1
                while k < l:
                    val = nums[i] + nums[j] + nums[k] + nums[l]
                    if val < target:
                        k += 1
                    elif val > target:
                        l -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k + 1 < l and nums[k] == nums[k + 1]:
                            k += 1
                        k += 1
                        while k + 1 < l and nums[l] == nums[l - 1]:
                            l -= 1
                        l -= 1
        return res