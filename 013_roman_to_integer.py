# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 00:52:12 2019

@author: zhang
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n, res, i = len(s), 0, 0
        while i < n:
            if i < n - 1 and dic[s[i]] < dic[s[i + 1]]:
                res -= dic[s[i]]
                res += dic[s[i + 1]]
                i += 2
            else:
                res += dic[s[i]]
                i += 1
        return res