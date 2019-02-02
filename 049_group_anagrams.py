# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:52:29 2019

@author: zhang
"""

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        return list(dic.values())