# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:49:27 2019

@author: zhang
"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        res = ""
        carry = 0
        for i in range(n1 + n2 - 1):
            low = i - (n2 - 1) if i > n2 - 1 else 0
            high = i if i < n1 - 1 else n1 - 1
            sum = carry
            for j in range(low, high + 1):
                sum += (ord(num1[n1 - 1 - j]) - ord('0')) * (ord(num2[n2 - 1 - (i - j)]) - ord('0'))
            carry = sum // 10
            sum %= 10
            res += str(sum)
        res += str(carry)
        while len(res) > 1 and res[-1] == '0':
            res = res[:-1]
        return res[::-1]