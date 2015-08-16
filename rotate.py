# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:14 2015

@author: Tianshu
"""

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        row=len(matrix);col=len(matrix[0])
        res=[[0 for cols in range(col)] for rows in range(row)]
        for i in range(row):
            for j in range(col):
                res[row-j][i]=matrix[i][j]
                