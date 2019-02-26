# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:54:42 2019

@author: zhang
"""

class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        w = words
        res = []
        nw = len(w)
        L = maxWidth
        i = 0
        while i < nw:
            j = i
            l = 0
            while j < nw:
                l += len(w[j])
                if l + j - i > L:
                    l -= len(w[j])
                    break
                j += 1
            line = ""
            if j - i == 1 or j == nw: #left justified
                while i < j:
                    line += w[i]
                    i += 1
                    line += ' '
                line = line[0 : -1]
                while len(line) < L:
                    line += ' '
            else:
                c1 = (L - l) // (j - i - 1)
                c2 = (L - l) % (j - i - 1)
                ci = 0
                while True:
                    line += w[i]
                    i += 1
                    if i == j: break
                    for k in range(c1): line += ' '
                    if ci < c2: line += ' '
                    ci += 1
            res.append(line)
        return res