# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:56:35 2019

@author: zhang
"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        comb, res = [], []
        def dfs(cand, target, l, comb, res):
            if not target:
                res.append(comb[::-1])
                return
            for i in range(l, len(cand)):
                if target < cand[i]: break
                comb.append(cand[i])
                dfs(cand, target - cand[i], i, comb, res)
                comb.pop()
        dfs(candidates, target, 0, comb, res)
        return res