# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:52:00 2019

@author: zhang
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(ans, s, 4, [])
        return ['.'.join(x) for x in ans]
        
    def dfs(self, ans, s, k, temp):
        if len(s) > k*3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3,len(s)-k+1)):
                if i==2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.dfs(ans, s[i+1:], k-1, temp+[s[:i+1]])
        
        