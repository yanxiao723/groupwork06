# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:02:45 2020

@author: yan
"""

class Node:
    def __init__(self):
        self.next = None
        self.data =None
class Lian:
    def __init__(self):
        self._head = Node()
    def append(self,data):#尾部
        cur = self._head
        new = Node()
        if self.is_empty():
            self._head.data = data
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = new
            new.data =data
    def ahead(self,data):#头部
        cur = self._head
        new = Node()
        if self.is_empty():
            self._head.data = data
        else:
            new.data = data
            new.next = cur
            self._head = new
            
    def insert(self,goal,data):#中间
        cur = self._head
        new =Node()
        if self.is_empty():
            self._head.data =data
        else:
            while cur.data != goal:
                cur =cur.next
            new.next = cur.next
            cur.next = new
            new.data =data
    def is_empty(self):#判空
        return not self._head.data
    def  remove(self,data):#删除
        cur = self._head
        if cur.data ==data:
            cur = cur.next
            self._head = cur
        while cur.data !=data:
            save =cur
            cur =cur.next
        save.next =None           
#a =Lian()
#a.append((3,5))
#a.append((7,3))
#a.append((1,0))
#b =Lian()
#b.append((1,5))
#b.append((-1,3))
#b.append((2,1))
#b.append((8,0))
a_i = input('公式1')#3x^5+7x^3+1
b_i = input('公式2')#x^5+x^3-x^2+1

def sor(a_i):
    for i in range(len(a_i)):
        if  (i+1 ==  len(a_i) and a_i[i]=='x') or (i+1<len(a_i) and a_i[i] =='x' and a_i[i+1] !='^'):
            a_i = a_i[0:i+1]+'^1'+a_i[i+1:]
    
    for i in range(len(a_i)):
        if a_i[0]=='x' :
            a_i= '1'+a_i
        if a_i[i] == 'x' and not a_i[i-1].isdigit():
            a_i = a_i[:i]+'1'+a_i[i:]
   # print(a_i)     
    a_save = []
    for i in range(len(a_i)):
        if a_i[i].isdigit():
            if a_i[i-1] == '-':
                a_save.append(-1*int(a_i[i]))
            else:
                a_save.append((int(a_i[i])))
    if len(a_save) %2 ==1:
        a_save.append(0)
    #print(a_save)
    return [(a_save[i*2],a_save[i*2+1])  for i in range(len(a_save)//2)]

a_list = sor(a_i)
b_list = sor(b_i) 
a = Lian()
b =Lian()
for i in a_list:
    a.append(i)    
for j in b_list:
    b.append(j)
cur_b = b._head
cur_a = a._head 
c = Lian()
     
#print(cur_a.data)   
#print('---9999999999999-')
#print(cur_b.data)
while cur_a!= None and cur_b!=None:
    #print(cur_a.data,cur_b.data)
    if cur_a.data[1] > cur_b.data[1]:
        c.append(cur_a.data)
        cur_a = cur_a.next
    elif cur_a.data[1]< cur_b.data[1]:
        c.append(cur_b.data)
        cur_b = cur_b.next
    else:
        if (cur_a.data[0]+cur_b.data[0]) != 0:
            c.append(((cur_a.data[0]+cur_b.data[0]),cur_a.data[1]))#若计算减法则把加号改为减号
        
        cur_a = cur_a.next
        cur_b = cur_b.next
    #print(cur_a.data)
    #print(cur_b.data)
if cur_a !=None or cur_b != None:
    if cur_a == None:
        c.append(cur_b.data)
    if cur_b == None:
        c.append(cur_a.data)
cur1 = c._head

str_sum =''
if not cur1.data:
    print(0)
else:
    while cur1:
        
        
        if   cur1.data[1]!=0:
            str_sum+=(str(cur1.data[0])+'x^'+str(cur1.data[1]))+'+'
        elif cur1.data[1] ==1:
                str_sum+=(str(cur1.data[0])+'x^'+str(cur1.data[1]))
                
        else:
            str_sum+='+'+str(cur1.data[0])
#        print(str_sum)   
#        print(cur1.data)
        
        cur1 = cur1.next
    if str_sum[-1] == '+':
        str_sum = str_sum[:-1]
    str_sum=str_sum.replace('++','+').replace('+-','-')
    
    print('result is '+str_sum)
    


##c._head.next.next.next.data  (2)	a(x)= 3x^5+7x^3+1
#b(x)=9x^6-7x^3+4x^2+5x-1
#加法运算结果：-3x^5-7x^3-1
#c(x)=9x^6+3x^5+4x^2+5x
#[(3,5),(7,3),(1,0)]     [(9,6),(-7,3),(4,2),(5,1),(-1,0)]
#    #x^4+x^2+1
#b(x)=x^5+x^3-x^2+1
#加法运算结果：
#c(x)=x^5+x^4+x^3+2





        


        
    
