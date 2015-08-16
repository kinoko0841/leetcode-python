# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 19:36:37 2015

@author: Tianshu
"""

class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        res=[];
        self.dfs(1,[],res,s)
        return res
        
    def dfs(self,depth,element,res,s):
        if len(element)==3:
            if int(s[0:element[0]+1])<=255 and int(s[(element[0]+1):element[1]+1])<=255 and int(s[(element[1]+1):element[2]+1])<=255 and int(s[(element[2]+1):11])<=255:
                str=s[0:element[0]+1]+'.'+s[element[0]+1:element[1]+1]+'.'+s[(element[1]+1):element[2]+1]+'.'+s[(element[2]+1):11]                
                res.append(str)
        if depth==10:
            return
        for i in range(depth,10):
            self.dfs(i+2,element+[i],res,s)

list="25525511135"
sol=Solution()
b=sol.restoreIpAddresses(list)
print b
