# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 21:49:51 2015

@author: Tianshu
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        #if len(num) == 0: return []
        #if len(num) == 1: return [num]
        ans=[];element=[]
        def dfs(depth,element,ans):
            if depth==len(num) and element not in ans:
                ans.append(element)
            for i in range(depth,len(num)):
                num[depth],num[i]=num[i],num[depth]
                dfs(depth+1,element+[num[depth]],ans)
                num[depth],num[i]=num[i],num[depth]
        dfs(0,element,ans)
        return ans

list=[1,2,3,4,4]
sol=Solution()
b=sol.permute(list)
print b
