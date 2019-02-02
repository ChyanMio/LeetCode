# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:26:31 2019

@author: zhang
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        ls, lp = len(haystack), len(needle)
        if ls < lp: return -1
        p = [0 for _ in range(lp)]
        for i in range(1, lp):
            p[i] = p[i - 1]
            while p[i] > 0 and needle[p[i]] != needle[i]:
                p[i] = p[p[i] - 1]
            if needle[p[i]] == needle[i]:
                p[i] += 1
            
        pre = 0
        for i in range(ls):
            while pre > 0 and needle[pre] != haystack[i]:
                pre = p[pre - 1]
            if needle[pre] == haystack[i]:
                pre += 1
            if pre == lp:
                return i - pre + 1
        return -1