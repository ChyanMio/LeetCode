# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:00:45 2019

@author: zhang
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import heapq
        heap = [(0, word1, word2)]
        seen = set()
        while heap:
            distance, w1,w2 = heapq.heappop(heap)
            if w1 == w2: return distance
            if (w1, w2) in seen: continue
            else: seen.add((w1, w2))
                
            if w1 and w2 and w1[-1] == w2[-1]:
                heapq.heappush(heap, (distance, w1[:-1], w2[:-1]))
            else:
                if w1: heapq.heappush(heap, (distance+1, w1[:-1], w2))
                if w2: heapq.heappush(heap, (distance+1, w1, w2[:-1]))
                if w1 and w2: heapq.heappush(heap, (distance+1, w1[:-1], w2[:-1]))