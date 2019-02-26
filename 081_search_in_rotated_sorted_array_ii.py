# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:52:40 2019

@author: zhang
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        ll, rr = 0, n - 1
        while ll <= rr:
            mm = ll + (rr - ll) // 2
            if nums[ll] < target and target < nums[mm]:
                rr = mm - 1
            elif nums[mm] < target and target < nums[rr]:
                ll = mm + 1
            else:
                if nums[ll] == target:
                    return True
                else:
                    ll += 1
                if nums[rr] == target:
                    return True
                else:
                    rr -= 1
        return False