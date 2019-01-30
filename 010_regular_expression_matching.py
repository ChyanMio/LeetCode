# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:04:37 2019

@author: zhang
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #backtracking
        ls, lp, i, j = len(s), len(p), 0, 0
        sc, si, sj = [], [], []
        while i < ls or j < lp:
            if j + 1 < lp and p[j + 1] == '*':
                sc.append(p[j])
                si.append(i)
                j += 2
                sj.append(j)
            elif i < ls and j < lp and (p[j] == '.' or s[i] == p[j]):
                i, j = i + 1, j + 1
            elif sc != []:
                k = si[-1]
                if k < ls and (sc[-1] == '.' or s[k] == sc[-1]):
                    k += 1
                    si[-1] = k
                    i = si[-1]
                    j = sj[-1]
                else:
                    sc.pop()
                    si.pop()
                    sj.pop()
            else: break
        return (i == ls) and (j == lp)
        
            
                    