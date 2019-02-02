# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:23:57 2019

@author: zhang
"""

import itertools
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for _ in range(n - 1):
            seq = ''.join(str(len(list(cnt))) + digit
                for digit, cnt in itertools.groupby(seq))
        return seq