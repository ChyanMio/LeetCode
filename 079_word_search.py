# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:36:54 2019

@author: zhang
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        b = board
        if not b or not b[0]: return False
        m, n, lw = len(b), len(b[0]), len(word)
        res = False
        visited = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(i, j, k):
            if i >= m or i < 0 or j >= n or j < 0 or visited[i][j] or word[k] != b[i][j]: return False
            if k == lw - 1: return  True
            visited[i][j] = 1
            res = dfs(i + 1, j , k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            visited[i][j] = 0
            return res
        for i in range(m):
            for j in range(n):
                if b[i][j] == word[0]: res = dfs(i, j, 0)
                if res: return True
        return False