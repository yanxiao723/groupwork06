# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:29:06 2020

@author: yan
"""
#1+8/4-6/2#，或5+(1+3-5)+(8-2)/3#
shi = input('输入末尾带#号的式子')
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
# 513+5-+
fir  = {'+':1,'-':1,'*':2,'/':2,'(':4,')':0}
str1 =''
b=zhan()
for i in shi:
    if i in fir :
        if a.is_empty():
            a.push(i)
            if i == '(':
                fir[i] = 0
                #print(a._list[a.top],'qwee')
        elif fir[i] <= fir[a._list[a.top]] :
            #print(i,fir[i],a._list[a.top])
            str1+=a.pop()
            a.push(i)
            if i ==')':
                a.pop()
                a.pop()
                fir['('] = 4
        elif fir[i] > fir[a._list[a.top]] :
            a.push(i) 
            if i == '(':
                #print(a._list[a.top])
                fir[i] = 0
    elif i == '#':
        while not a.is_empty():       
            str1+=a.pop()
    elif i.isdigit():
        str1+=i
#print(str1)
for i in str1:
    if i in fir:
        b.push(i)
        q,w,e = b.pop(),b.pop(),b.pop()#/28
        #print(q,w,e)
        b.push(str(eval(e+q+w)))
    else:
        b.push(i)
print(b.pop())



        
        
        

            
            
        
       
        
        
        

    
                
    
                
                
    



    



            
            
        
        
        
        
        
        
