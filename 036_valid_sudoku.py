# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:21:27 2019

@author: zhang
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[False for _ in range(9)] for _ in range(9)]
        col = [[False for _ in range(9)] for _ in range(9)]
        block = [[False for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                d = eval(board[i][j]) - 1
                if row[i][d]: return False
                row[i][d] = True
                if col[j][d]: return False
                col[j][d] = True
                if block[i // 3 * 3 + j // 3][d]: return False
                block[i // 3 * 3 + j // 3][d] = True
        return True