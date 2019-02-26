# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:17:03 2019

@author: zhang
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if len(intervals) <= 1: return intervals
        intervals = sorted(intervals, key = lambda a: a.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1].end < intervals[i].start: res.append(intervals[i])
            else: res[-1].end = max(res[-1].end, intervals[i].end)
        return res