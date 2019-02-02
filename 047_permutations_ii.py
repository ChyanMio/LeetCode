# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:37:13 2019

@author: zhang
"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            tmp = []
            for lis in res:
                for i in range(len(lis) + 1):
                    tmp.append(lis[:i] + [num] + lis[i:])
                    if i < len(lis) and lis[i] == num: break
            res = tmp
        return res