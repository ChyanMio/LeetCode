# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:22:59 2019

@author: zhang
"""

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.pos = []
        self.row = [0 for _ in range(9)]
        self.col = [0 for _ in range(9)]
        self.block = [0 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.pos.append(i * 9 + j)
                else:
                    self.mark(i, j, eval(board[i][j]))
        self.dfs(board)
        
    def mark(self, i, j, k):
        bt = (1 << k - 1)
        self.row[i] ^= bt
        self.col[j] ^= bt
        self.block[i // 3 * 3 + j // 3] ^= bt
    
    def dfs(self, board):
        if not self.pos: return True
        idx = self.pos[-1]
        x, y = idx // 9, idx % 9
        for d in range(1, 10):
            bt = (1 << d - 1)
            if self.row[x] & bt: continue
            if self.col[y] & bt: continue
            if self.block[x // 3 * 3 + y // 3] & bt: continue 
            self.pos.pop()
            self.mark(x, y, d)
            board[x][y] = str(d);
            if(self.dfs(board)): return True
            board[x][y] = '.'
            self.mark(x, y, d);
            self.pos.append(idx)
        return False      