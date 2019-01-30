# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:09:36 2019

@author: zhang
"""

class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = len(s)
        res, i = 0, 0
        while i < ls and s[i] == ' ': i += 1
        if i >= ls or s[i] not in "0123456789-+": 
            return res
        flag = 1
        if s[i] == '+':
            flag = 1
            i += 1
        elif s[i] == '-':
            flag = -1
            i += 1
        while i < ls:
            if(s[i] not in "0123456789"):
                return flag * res;
            res = res * 10 + (ord(s[i]) - ord('0'))
            if flag * res < -2147483648:
                return -2147483648
            if flag * res > 2147483647:
                return 2147483647
            i += 1
        return flag * res