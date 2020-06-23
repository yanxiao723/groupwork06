# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:50:24 2020

@author: yan
"""
m = eval(input('qwe'))
n = eval(input('zxc'))

list1 = list(range(1,m+1)) 
count =0 
total = 0
save =[]
i=0
print(m,n,list1)
while total != m:
    if count ==n:
        save.append(list1[i-1])
        list1[i-1] =0
        count=0
        total+=1
    else:
        if list1[i] == 0:
            i+=1
        else:
            i+=1
            count+=1
        if i == m:
            i=0
print(save)

        
        
        
    
