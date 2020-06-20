# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:44:59 2020

@author: yan
"""
graph  = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
def dfs(adj,start):
    stack =[[start,0]]
    er = set()
    print(start)
    while stack:
        vector,index = stack[-1]
        
        if vector not  in adj or index >= len(adj[vector]):
            stack.pop()
            continue
        
        value = adj[vector][index]
        stack[-1][1]+=1
        if value in er:
            continue
        print(value)
        er.add(value)
        stack.append([value,0])
dfs(graph,1)
    
        
        
        
        
    
