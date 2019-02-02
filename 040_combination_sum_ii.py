# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:04:21 2019

@author: zhang
"""

class Solution:
    def combinationSum2(self, candidates, target):
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
                if i != l and cand[i] == cand[i - 1]: continue
                comb.append(cand[i])
                dfs(cand, target - cand[i], i + 1, comb, res)
                comb.pop()
        dfs(candidates, target, 0, comb, res)
        return res