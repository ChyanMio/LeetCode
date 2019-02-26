# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:01:59 2019

@author: zhang
"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results