# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:27:35 2019

@author: zhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(0)
        carry = 0
        while l1 and l2:
            carry, sum  = divmod(carry + l1.val + l2.val, 10)
            l3.next = ListNode(sum)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        while l1:
            carry, sum  = divmod(carry + l1.val + 0, 10)
            l3.next = ListNode(sum)
            l1 = l1.next
            l3 = l3.next
        while l2:
            carry, sum  = divmod(carry + l2.val + 0, 10)
            l3.next = ListNode(sum)
            l2 = l2.next
            l3 = l3.next
        if carry:
            l3.next = ListNode(carry)
        return head.next
        