# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:28:39 2019

@author: zhang
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numbers = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def dfs(s, digits, res):
            idx = len(s)
            if idx == len(digits):
                res.append(s)
                return
            d = ord(digits[idx]) - ord('0')
            for i in range(len(numbers[d])):
                dfs(s + numbers[d][i], digits, res)
                
        res = []
        if digits == "": return res
        dfs("", digits, res)
        return res