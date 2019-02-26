# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:10:15 2019

@author: zhang
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            cnt = 0
            while cnt + i < len(nums) and nums[cnt + i] == nums[i]:
                cnt += 1
            n = len(res)
            for j in range(n):
                tmp = res[j][::]
                for k in range(cnt):
                    tmp.append(nums[i])
                    res.append(tmp[::])
            i += cnt
        return res