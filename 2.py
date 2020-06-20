# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:33:45 2020

@author: yan
"""

class Node():
    def __init__(self,data):
        self.pre = None
        self.next = None
        self.elem = data

class Lian():
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
    def append(self,data):
        node =Node(data)
        if self.is_empty():
            self._head =node
            node.next =node
            node.pre =node
        else:
            node.pre = self._head.pre
            node.next = self._head
            self._head.pre.next = node
            self._head.pre = node
            
            
    def remove(self,data):
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.elem == data:
                if cur.next ==self._head:
                    self._head = None
                else:
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                    self._head = cur.next
            else:
                cur = cur.next
                while cur is not self._head:
                    if cur.elem == data:
                        cur.next.pre = cur.pre
                        cur.pre.next = cur.next
                    cur = cur.next


m = Lian()
m1= eval(input('m'))
n=eval(input('n'))

#m._head.next.next.elem
for i in range(1,m1+1):
    m.append(i)

save=[]
count =1
k  =0
cur =m._head
while  not m.is_empty():
    
    while count!= n:
        
        cur =cur.next
        count+=1
        print(cur.elem,count)
        print('------------------------------')
    else:
        print(cur.elem)
        save.append(cur.elem)
        m.remove(cur.elem)
        print('**************')
        print(cur.elem)
        count=0
        
    k+=1
    
    
        
print(save)        




