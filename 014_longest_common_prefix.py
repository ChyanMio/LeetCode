# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 00:57:31 2019

@author: zhang
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0: return ""
        res = strs[0]
        for i in range(1, n):
            l = len(res)
            for j in range(l):
                if j >= len(strs[i]) or strs[i][j] != res[j]:
                    res = res[0 : j]
                    break
        return res