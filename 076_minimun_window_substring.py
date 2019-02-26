# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:01:25 2019

@author: zhang
"""

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #sliding window problem
        ls, lt = len(s), len(t)
        if not lt or ls < lt: return ""
        cnt = 0
        vs, vt = [0]*256, [0]*256
        for i in range(lt):
            vt[ord(t[i])] +=1
            cnt += 1
        min_len, res = ls + 1, ""
        j = 0
        for i in range(ls):
            if vs[ord(s[i])] < vt[ord(s[i])]:
                cnt -= 1
            vs[ord(s[i])] += 1
            if cnt > 0: continue
            ch = s[j]
            j += 1
            vs[ord(ch)] -= 1
            while vs[ord(ch)] >= vt[ord(ch)]:
                ch = s[j]
                j += 1
                vs[ord(ch)] -= 1
            cnt += 1
            if i - j + 2 < min_len:
                min_len = i - j + 2
                res = s[j - 1: j  - 1 + min_len]
        return res