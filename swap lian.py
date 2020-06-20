# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:12:17 2020

@author: yan
"""
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
class Lian:
    def __init__(self,head = None):
        self.head  =head
    def append(self,data):
        cur = self.head
        if cur is None:
            self.head = Node(data)
        else:
            while cur.next:
                cur =cur.next
            cur.next = Node(data)
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def swap(self,data1,data2):
        if data1 == data2:
           return 
        z1 = self.head
        prez1 = None
        while z1 is not None and z1.data!= data1:
            prez1 =z1
            z1 = z1.next
        z2 = self.head
        prez2 = None
        while z2 is not None and z2.data!= data2:
            prez2 = z2
            z2 = z2.next
        if z1 is None and z2 is None:
            return 
        if prez1 is None:
            self.head = z2
        else:
            prez1.next =z2
        if prez2 is None :
            self.head = z2
        else:
            prez2.next =z1
        tmp =z1.next
        z1.next = z2.next
        z2.next =tmp

        
            
            
        
            
            
a =Lian()
for i in range(2):
    a.append(i)
a.print_list()
a.swap(1,0)
