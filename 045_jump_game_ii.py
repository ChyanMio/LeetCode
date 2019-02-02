# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:25:11 2019

@author: zhang
"""

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return 0
        i, pos, cnt = 0, 0, 0
        while True:
            new_pos = pos
            while i <= pos:
                new_pos = max(new_pos, i + nums[i])
                i += 1
            cnt += 1
            pos = new_pos
            if pos >= n - 1: break
        return cnt