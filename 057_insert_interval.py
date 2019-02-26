# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:21:32 2019

@author: zhang
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        it, ni = intervals, newInterval
        n, i = len(it), 0
        res = []
        while i < n and it[i].end < ni.start:
            res.append(it[i])
            i += 1
        while i < n and it[i].start <= ni.end:
            ni.start = min(ni.start, it[i].start)
            ni.end = max(ni.end, it[i].end)
            i += 1
        res.append(ni)
        while i < n:
            res.append(it[i])
            i += 1
        return res