# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:48:03 2019

@author: zhang
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        files = [f for f in path.split('/') if f != '.' and f != '']
        stack = []
        for f in files:
            if f == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(f)
        return '/' + '/'.join(stack)