# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:52:30 2019

@author: zhang
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, s_mark, p_mark = 0, 0, -1, -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1; j += 1
            elif j < len(p) and p[j] == '*':
                s_mark, p_mark = i, j
                j += 1
            elif p_mark != -1:
                s_mark += 1
                i, j = s_mark, p_mark + 1
            else:
                return False
        while j < len(p) and p[j] == '*': j += 1 #match when s is empty
        return True if j == len(p) else False
        