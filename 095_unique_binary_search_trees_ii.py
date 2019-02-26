# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:53:29 2019

@author: zhang
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        def dfs(left, right, res):
            if left > right:
                res.append(None)
                return res
            for i in range(left, right + 1):
                left_res = dfs(left, i - 1, [])
                right_res = dfs(i + 1, right, [])
                ll, lr = len(left_res), len(right_res)
                for j in range(ll):
                    for k in range(lr):
                        root = TreeNode(i)
                        root.left = left_res[j]
                        root.right = right_res[k]
                        res.append(root)
            return res
        return dfs(1, n, [])