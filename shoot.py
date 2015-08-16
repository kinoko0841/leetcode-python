# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:02:17 2015
问题是：一个射击运动员打靶,靶一共有10环,连开10枪打中90环的可能有哪些
如果问题问多少种，也是一样解法
@author: Tianshu
"""


class Solution:
    def shoot(self,num,score,sum):
        def dfs(depth,path,res,sum):
            if len(path)==num and sum==0:
                res.append(path)
                return res
            for i in range(depth,score+1):
                if sum<i:
                    return
                dfs(depth,path+[i],res,sum-i)
                #print path
        path=[]
        res=[]
        dfs(1,path,res,sum)
        return res

    def combinationSum(self, candidates, target):
        res=[];candidates.sort()
        self.combdfs(0,[],res,candidates,target)
        return res
        
    def combdfs(self,depth,element,res,candidates,target):
        if target==0:
            res.append(element)
        if depth==len(candidates):
            return
        for j in range(depth,len(candidates)):
            if target < candidates[j]:
                return
            self.combdfs(depth+1,element+[candidates[j]],res,candidates,target-candidates[j])

a=Solution()
#print a.shoot(3,3,4)
print a.combinationSum([2,3,4,6,7],7)