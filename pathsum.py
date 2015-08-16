# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:29:28 2015

@author: Tianshu
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root==None:return False
        def dfs(root,pathsum):
            if root==None:
                return False
            if root.left==None or root.right==None:
                return pathsum==sum
            if root.left!=None:
                dfs(root.left,pathsum+root.left.val)
            if root.right!=None:
                dfs(root.right,pathsum+root.right.val)
        dfs(root,root.val)

node1=TreeNode(1)
node2=TreeNode(2)
root=TreeNode(0)