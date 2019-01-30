# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:00:22 2019

@author: zhang
"""
#bisection method
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            l1, l2, nums1, nums2 = l2, l1, nums2, nums1
        lo, hi, m = 0, l1, (l1 + l2 + 1) // 2
        while lo <= hi:
            i = (lo + hi) // 2
            j = m - i
            if i < l1 and nums2[j - 1] > nums1[i]:
                lo = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                hi = i - 1
            else:
                if i == 0: leftMax = nums2[j - 1]
                elif j == 0: leftMax = nums1[i - 1]
                else: leftMax = max(nums1[i - 1], nums2[j - 1])
                
                if (l1 + l2) % 2: return leftMax
                
                if i == l1: rightMin = nums2[j]
                elif j == l2: rightMin = nums1[i]
                else: rightMin = min(nums1[i], nums2[j])
                
                return (rightMin + leftMax) / 2