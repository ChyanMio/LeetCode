# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:15:21 2019

@author: zhang
"""
import collections
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words: return []
        dic = dict(collections.Counter(words))
        ls, l, lp = len(s), len(words), len(words[0])
        res = []
        for i in range(ls - lp * l + 1):
            rec, j = {}, 0
            while j < l:
                word = s[i + j * lp : i + (j + 1) * lp]
                if word in dic:
                    rec[word] = rec.get(word, 0) + 1
                    if rec[word] > dic[word]:
                        break
                else: break
                j += 1
            if j == l: res.append(i)
        return res