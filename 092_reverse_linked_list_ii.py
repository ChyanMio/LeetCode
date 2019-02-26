# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:28:07 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        n -= m
        dummy = pre = ListNode(0)
        pre.next = head
        m -= 1
        while m:
            pre = pre.next
            m -= 1
        cur = pre.next
        while n:
            p = cur.next
            cur.next = p.next
            p.next = pre.next
            pre.next = p
            n -= 1
        return dummy.next
    