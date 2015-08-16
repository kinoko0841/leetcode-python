# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 10:47:57 2015

@author: Tianshu
"""
n=79927398717
arr=[]
while n:
    arr.append(n%10)
    n/=10
if len(arr)%2==0:
    for i in range(0,len(arr),2):
        arr[i]*=2
        if arr[i]>9:arr[i]-=9
if len(arr)%2==1:
    for i in range(1,len(arr),2):
        arr[i]*=2
        if arr[i]>9:arr[i]-=9
if sum(arr)%10==0:print True
else: print False