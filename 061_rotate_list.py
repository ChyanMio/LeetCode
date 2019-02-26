# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:32:01 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if not k or not head: return head
        n, cur = 0, head
        while cur:
            cur = cur.next
            n += 1
        if not k % n: return head
        k %= n
        cur = head
        for i in range(1, n - k):
            cur = cur.next
        h = cur.next
        cur.next = None
        t = h
        while t.next:
            t = t.next
        t.next = head
        return h