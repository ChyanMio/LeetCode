# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 19:27:26 2019

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
        q = 373591679
        ls, lp = len(haystack), len(needle)
        if ls < lp: return -1
        d, t, p, h = 3, ord(haystack[0]), ord(needle[0]), 1
        for i in range(1, lp):
            h = (h * d) % q
            p = (p * d + ord(needle[i])) % q
            t = (t * d + ord(haystack[i])) % q
        for i in range(ls - lp + 1):
            if p == t:
                j = 0
                while j < lp and needle[j] == haystack[i + j]:
                    j += 1
                if j == lp: return i
            if i < ls - lp:
                t = ((t - ord(haystack[i]) * h) * d + ord(haystack[i + lp])) % q
        return -1