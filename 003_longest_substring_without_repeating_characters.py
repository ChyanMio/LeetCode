# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:28:05 2019

@author: zhang
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = [0 for i in range(256)]
        res = 0
        j = 0
        for i in range(len(s)):
            index = ord(s[i])
            dic[index] += 1
            while dic[index] > 1:
                dic[ord(s[j])] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res