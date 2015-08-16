# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:28:13 2015

@author: Tianshu
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row=[];col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row+=[i]
                    col+=[j]
        
        for i in row:
            for z in range(len(matrix[0])):
                matrix[i][z]=0
        for k in range(len(matrix)):
            for j in range(len(col)):
                matrix[k][col[j]]=0


sol=Solution()
list=[[1,1,1],[1,0,1],[1,1,1]]
print sol.setZeroes(list)