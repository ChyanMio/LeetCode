# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:33:47 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #two dummy nodes to avoid creating new node
        left = left_dummy = ListNode(0)
        right = right_dummy = ListNode(0)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = right_dummy.next
        return left_dummy.next
    