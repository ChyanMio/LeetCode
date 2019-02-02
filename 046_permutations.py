# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:32:37 2019

@author: zhang
"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #dfs
        def dfs(nums, lis, res):
            if not nums:
                res.append(lis)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], lis + [nums[i]], res)
        res = []
        dfs(nums, [], res)
        return res