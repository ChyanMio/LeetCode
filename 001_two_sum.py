# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:34:08 2019

@author: zhang
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i in range(len(nums)):
            if hashTable.get(target - nums[i], -1) != -1:
            # if target - nums[i] in hashTable:
                return [hashTable[target - nums[i]], i]
            else:
                hashTable[nums[i]] = i