# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:02:05 2015

@author: Tianshu
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        arr=[[0 for x in range(n)] for y in range(n)]
        x=0;y=0;i=1
        while x<n and y<n and i<=n*n:
                 #arr[x][y]=i;i+=1
                if arr[x][y]==0 and y+1<n and (x==0 or (arr[x-1][y]!=0)):
                    arr[x][y]=i;i+=1;y+=1
                elif arr[x][y]==0 and x+1<n and (y==n-1 or (arr[x][y+1]!=0)):
                    arr[x][y]=i;i+=1;x+=1
                elif arr[x][y]==0 and y-1>=0 and (x==n-1 or (arr[x+1][y]!=0)):
                    arr[x][y]=i;i+=1;y-=1
                elif arr[x][y]==0 and x-1>=0 and (y==0 or (arr[x][y-1]!=0)):
                    arr[x][y]=i;i+=1;x-=1
        return arr
sol=Solution()
b=sol.generateMatrix(4)