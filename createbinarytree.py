# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:23:59 2015

@author: Tianshu
"""

class TreeNode(object):

    def __init__(self, left=0, right=0, val=0):
        self.left = left
        self.right = right
        self.val = val

class BTree(object):

    def __init__(self, root=0):
        self.root = root

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root,sum):
        res=[]
        #if root==None:return False
        def dfs(root,res):
            if root!=None:
                res.append(root.val)
                dfs(root.left,res)
                dfs(root.right,res)
        dfs(root,res)
        return res

node1 = TreeNode(None,None,val=1)
node2 = TreeNode(node1, 0, 2)
node3 = TreeNode(None,None,val=3)
node4 = TreeNode(None,None,val=4)
node5 = TreeNode(node3, node4, 5)
node6 = TreeNode(node2, node5, 6)
node7 = TreeNode(node6, 0, 7)
node8 = TreeNode(None,None,val=8)
root = TreeNode(node7, node8, 0)
bt = BTree(root)
sol=Solution()
print root.right.val
print sol.hasPathSum(root,0)

