# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 02:22:29 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val:
            return self.mergeTwoLists(l2, l1)
        l3 = l1
        l4 = l3
        l1 = l1.next
        while l1 and l2:
            if l1.val < l2.val:
                l4.next = l1
                l1 = l1.next
            else:
                l4.next = l2
                l2 = l2.next
            l4 = l4.next
        if l1:
            l4.next = l1
        if l2:
            l4.next = l2
        return l3