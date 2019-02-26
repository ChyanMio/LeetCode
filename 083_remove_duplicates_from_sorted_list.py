# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:10:12 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next