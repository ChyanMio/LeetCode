# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:35:10 2019

@author: zhang
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #catalan number
        #dp method
        res = [[""]]
        for i in range(1, n + 1):
            tmp = []
            for j in range(i):
                for a in res[j]:
                    for b in res[i - 1 - j]:
                        tmp.append('(' + a + ')' + b)
            res.append(tmp)
        return res[-1]