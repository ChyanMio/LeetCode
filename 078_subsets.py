# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:23:43 2019

@author: zhang
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in sorted(nums):
            res += [n + [num] for n in res]
        return res