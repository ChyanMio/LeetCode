# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:33:50 2019

@author: zhang
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            cnt = 0
            while r and cnt < k:
                r = r.next
                cnt += 1
            if cnt == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
            

