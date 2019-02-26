# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:17:30 2019

@author: zhang
"""

class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        if not s: return 0
        i = len(s) - 1
        while  i >= 0 and s[i] == ' ': i -= 1
        l = 0
        while i >= 0 and s[i] != ' ':
            i -= 1
            l += 1
        return l