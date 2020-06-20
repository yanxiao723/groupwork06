# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:26:00 2020

@author: yan
"""

class big_heap:
    def __init__(self):
        self.list = []
    def get_parent(self,index):
        if index == 0 or index >len(self.list)-1 :
            return None
        else:
            return (index-1) >> 1
    def swap(self,index1,index2):
        self.list[index1] ,self.list[index2] = self.list[index2] ,self.list[index1]
    def insert(self,data):
        
        self.list.append(data)
        index = len(self.list)-1
        parent = self.get_parent(index)
        while parent is not None and self.list[index] >self.list[parent]:
            self.swap(index,parent)
            index = parent
            parent = self.get_parent(parent)
    def remove_Max(self):
        re = self.list[0]
        self.list[0] = self.list[-1]
        del self.list[-1]
        self.heapify(0)
        return re
            
    def heapify(self,index):
        
        while True:
            maxindex = index
            if 2*index+1 <len(self.list) and self.list[maxindex]< self.list[2*index+1]:
                maxindex = 2*index+1
            if  2*index+2 <len(self.list) and self.list[maxindex]< self.list[2*index+2]:
                maxindex = 2*index+2
            if maxindex ==index:
                break
            self.swap(index,maxindex)
            index = maxindex
        
        
            
            

def dfs(adj, start):
    visited = set()
    stack = [[start, 0]]
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])
 
 
graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
dfs(graph, 1)
   
        
        
        
        
        
a=big_heap()
for i in range(1,11):
    
    a.insert(i)
a.list
a.remove_Max()
a.list
m =[]
m[-1][1] = 4
    
        