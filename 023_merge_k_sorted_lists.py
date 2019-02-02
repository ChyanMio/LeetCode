# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:50:08 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        cur = head
        h, index = [], 0
        for node in lists:
            if node:
                h.append((node.val, index, node))
            index += 1 #index is used to avoid comparing between two ListNodes
        heapq.heapify(h)
        while h:
            _, _, n = h[0] 
            if n.next is None:
                heapq.heappop(h)
            else:
                heapq.heapreplace(h, (n.next.val, index, n.next))
                index += 1
            cur.next = n
            cur = cur.next
        return head.next