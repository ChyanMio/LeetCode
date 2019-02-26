# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:04:36 2019

@author: zhang
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(idx, v):
            if len(v) == k:
                res.append(v)
                return 
            for i in range(idx, n + 2 - k + len(v)):
                dfs(i + 1, v + [i])
        dfs(1, [])
        return res
    
    #return list(itertools.combinations([x for x in range(1, n+1)], k))