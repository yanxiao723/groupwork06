# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:38:31 2020

@author: yan
"""
shi = input('输入式子(末尾不用带#号)')
class zhan:
    def __init__(self):
        self._list=[]
        self.top = 0
        
    def push(self,data):
        
        if self.is_empty():
            self._list.append(data)
        else:
            self._list.append(data)  
            self.top+=1
    def is_empty(self):
        return   len(self._list) == 0
    def length(self):
        return len(self._list)
    def pop(self):
        if  self.is_empty():
            return 'error'
        elif self.length() >1:
            cur = self._list.pop()
            self.top-=1
            return cur
        else:
            cur = self._list.pop()
            return cur
    
a = zhan()
cc =False
b =zhan()
bb = False
def zhuan(i):
    global cc
    if i in ['*','/']:
        cc = True
        a.push(i)
    else:
        a.push(i)
        if cc :
            q,w,e  = a.pop(),a.pop(),a.pop()
            a.push(str(eval(e+w+q)))
            cc =False
def jia(d):    
    #print(d._list)
    while d.length() >1:
        q,w,e  = d.pop(),d.pop(),d.pop()
        d.push(str(eval(e+w+q)))
    return d.pop()

for i in shi:
    if i != '(' and not bb:
        zhuan(i)
        
    else:
        bb = True
        if i !=')' and bb :
            if i != '(':
                b.push(i) 
            #print(b._list)
        elif i==')':

            k=jia(b)
            a.push(k)
            b = zhan()
            bb = False
else:
    print(jia(a))

