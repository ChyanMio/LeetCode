# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 18:43:32 2019

@author: zhang
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        new_head = head.next
        new_tail = head
        head = head.next.next
        new_head.next = new_tail
        new_tail.next = None #necessary
        
        while head and head.next:
            p1 = head
            p2 = head.next
            head = head.next.next
            new_tail.next = p2
            p2.next = p1
            new_tail = p1
            new_tail.next = None #necessary
        if head:
            new_tail.next = head
            new_tail = head
            new_tail.next = None #necessary
        return new_head