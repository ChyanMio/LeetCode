# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:29:40 2019

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
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
        #reference:https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28336/Python-in-place-solution-with-dummy-head-node