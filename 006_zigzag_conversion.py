# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:30:12 2019

@author: zhang
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s): return s #boring board case
        t, i = "", 0
        while i < len(s):
            t += s[i]
            i += 2 * numRows - 2
            
        for i in range(1, numRows - 1):
            t += s[i]
            j = 2 * numRows - i - 2
            while j < len(s):
                t += s[j]
                if j + 2 * i < len(s): t += s[j + 2 * i]
                j += 2 * numRows - 2
                
        i = numRows - 1
        while i < len(s):
            t += s[i]
            i += 2 * numRows - 2
        return t