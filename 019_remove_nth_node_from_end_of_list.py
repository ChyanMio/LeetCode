# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:54:55 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cnt = n + 1
        p1 = head
        while p1 and cnt > 0:
            p1 = p1.next
            cnt -= 1
        if cnt > 0:
            head = head.next
            return head
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head