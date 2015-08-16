# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:21:26 2015

@author: Tianshu
"""

class Node:
  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

class Solution:
  def VisitTree_Recursive(self,root, order):
      if root:
          if order == 'NLR': print(root.data)
          self.VisitTree_Recursive(root.left, order)
          if order == 'LNR': print(root.data)
          self.VisitTree_Recursive(root.right, order)
          if order == 'LRN': print(root.data)
  def hasPathSum1(self, root, sum):
      if root == None:
          return False
      if root.left == None and root.right == None:
          print root.data
          return root.data == sum
      return self.hasPathSum1(root.left, sum - root.data) or self.hasPathSum1(root.right, sum - root.data)
      
  def hasPathSum(self, root, sum):
      def dfs(root,pathsum):
          if root!=None:
              print root.data
              pathsum+=root.data
              if pathsum==sum:
                  return True
              dfs(root.left,pathsum)
              dfs(root.right,pathsum)
      dfs(root,0)
    
  def preorderTraversal(self, root):
      res=[]
      def preorder(root,res):
          if root==None:return
          if root!=None:
              res.append(root.data)
              preorder(root.left,res)
              preorder(root.right,res)
      preorder(root,res)
      return res
  
  def preorderTraversal2(self, root):
      res=[]
      def preorder(root,path):
          if root==None:return False
          if root!=None:
              #print path
              path+=root.data
              print path
              #res.append(path)
              preorder(root.left,path)
              preorder(root.right,path)
      preorder(root,0)
      return res
  
  def maxDepth(self, root):
      if root==None:return 0
      else:
          return max(self.maxDepth(root.right),self.maxDepth(root.left))+1

  
  def isBalanced(self, root):
      if not root:
        return True
      return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
  
  def sumNumbers(self, root):
      def sum_numbers_help(root, curr):
          if not root:
              return 0
          if not root.left and not root.right:
              return 10 * curr + root.data
          return sum_numbers_help(root.left, 10 * curr + root.data) + sum_numbers_help(root.right, 10 * curr + root.data)
      return sum_numbers_help(root, 0)
  
  def pathsum2(self,root,sum):
      def dfs(root,path,pathsum,res):
          if not root.left and not root.right and pathsum+root.data==sum:
              print root.data
              path.append(root.data)
              res.append(path)
          if root.left:
              dfs(root.left,path+[root.data],pathsum+root.data,res)
          if root.right:
              dfs(root.right,path+[root.data],pathsum+root.data,res)
      if not root:
        return []
      res = []
      dfs(root, [], 0, res)
      return res
  
  def rightSideView(self, root):
      path = []
      def dfs(root,path):
          #print root.data
          if not root:
              return 0
          if not root.left and not root.right:
              #print path+root.data
              return path+[root.data]
          if root.right:
              return dfs(root.right,path+[root.data])
      return dfs(root,path)
          
g = Node(1)
h = Node(2)
e = Node(3, g, h)
i = Node(4)
f = Node(5, None, i)
c = Node(6, e, f)
d = Node(7)
b = Node(8, d)
a = Node(9, b, c)
root = a
sol=Solution()
arr=[1,2,3,4,5,6,7]
#print sol.VisitTree_Recursive(root,'LNR')
#print root
#print sol.hasPathSum(root,19)
#print sol.preorderTraversal(root)
#print sol.isBalanced(root)
#print sol.sumNumbers(root)
#print sol.pathsum2(root,20)
print sol.rightSideView(root)