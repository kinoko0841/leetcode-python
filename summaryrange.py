# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:32:50 2015

@author: Tianshu
"""

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if nums==[]:return []
        if len(nums)==1:return [str(nums[0])]
        min=nums[0];
        res=[]
        i=1
        str1=""
        while i<len(nums)-1:
            if nums[i]-nums[i-1]>1:
                max=nums[i-1]
                str1=str(min)+"->"+str(max)
                res.append(str1)
                min=nums[i]
            i+=1
        return res

sol=Solution()
print sol.summaryRanges([0,1,2,4,5,7])