# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:11:32 2019

@author: zhang
"""

class Solution:
    def isNumber(self, s: 'str') -> 'bool':
        ls = len(s)
        digits = "0123456789" 
        i, j = 0, ls - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        while i < j and s[i] == ' ':
            i += 1
        if i > j: return False
        s = s[i : j + 1]
        ls = len(s)
        pd, pe, cd, ce = -2, -2, 0, 0
        for k in range(ls):
            if s[k] == '.':
                pd = k
                cd += 1
            elif s[k] == 'E' or s[k] == 'e':
                pe = k
                ce += 1
            elif s[k] in digits:
                continue
            elif (s[k] == '+' or s[k] == '-') and (k == 0 or pe == k - 1):
                continue
            else:
                return False
        if cd > 1 or ce > 1:
            return False
        if cd == 1 and ce == 1 and pd > pe:
            return False
        if cd == 1:
            k = pd - 1
            cc = 0
            while k >= 0 and s[k] in digits:
                k -= 1
                cc += 1
            k = pd + 1
            while k < ls and s[k] in digits:
                k += 1
                cc += 1
            if cc == 0: return False
        if ce == 1:
            if pe == 0 or pe == 1 and (s[0] == '+' or s[0] == '-'):
                return False
            k = ls - 1
            cc = 0
            while k > pe and s[k] in digits:
                k -= 1
                cc += 1
            if cc == 0: return False
        if cd == 0 and ce == 0:
            k = ls - 1
            cc = 0
            while k >= 0 and s[k] in digits:
                k -= 1
                cc += 1
            if cc == 0: return False
        return True