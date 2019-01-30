# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 00:48:25 2019

@author: zhang
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        letters = "IVXLCDM"
        comb = ["", "0", "00", "000", "01", "1", "10", "100", "1000", "02"]
        base = 1000
        res = ""
        j = len(letters) - 1
        while base > 0:
            d = num // base
            num  = num % base
            base  = base // 10
            l = len(comb[d])
            for i in range(l):
                res += letters[j + ord(comb[d][i]) - ord('0')]
            j  = j - 2
        return res