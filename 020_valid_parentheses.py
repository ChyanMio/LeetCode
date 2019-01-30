# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 02:09:09 2019

@author: zhang
"""

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        lp, rp = "([{", ")]}"
        pair = {')':'(', ']':'[', '}':'{'}
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] in lp:
                stack.append(s[i])
                print(stack)
            elif s[i] in rp and stack and stack[-1] == pair[s[i]]:
                stack.pop()
                print(stack)
            else:
                break
        print(i)
        return i == n and not stack
isValid("()")