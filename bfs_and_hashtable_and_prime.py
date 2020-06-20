# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:05:48 2020

@author: yan
"""
graph  = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
def bfs(adj,start):
    er =set()
    stack = [start]
    
    er.add(start)
    while stack:
        value = stack.pop(0)
        for i in adj[value]:
            if i not in er:
                er.add(i)
                print(i)
                stack.append(i)
bfs({'0': ['1', '2', '3'], '1': ['0', '3'], '2': ['0', '3'], '3': ['0', '1', '2']},'0')
bfs(graph,1)
def fin(num):
    for i in range(2,num):
        if num%i == 0:
            print(i)
fin(48)

import math
def select(num):#mine_try
    
    list1= [i for i in range(3,num+1)]
    for i in list1:
        if i%2 == 0:
            list1[list1.index(i)]= -1*i
    for m in range(math.floor(math.sqrt(len(list1)))):
        if list1[m]>0:
            k = list1[m]
            #print(k)
            n=1
            while n*k <max([abs(i) for i in list1]):
                n+=1
                if n*k in list1:
                    list1[list1.index(n*k)] = -n*k
    return [i for i in list1 if i>0]
select(48)
import math

def find_prime_2(num):#book_show
    primes_bool = [False, False]+[True]*(num-1)
    for i in range(3,len(primes_bool)):
        # 将数组下标是偶数的数字全部置为否定状态
        if i%2 == 0:
            primes_bool[i] = False
    for i in range(3, int(math.sqrt(num))+1):
        # 如果当前数字处于被肯定的状态，则将其倍数的数字状态置为否定
        if primes_bool[i] is True:
            for j in range(i+i, num+1, i):
                primes_bool[j] = False
    prims = []
    # enumerate 将 primes_bool 组合成一个索引序列，i 是索引，v 是元素
    for i, v in enumerate(primes_bool):
        #　将判断为 True 的元素添加进 prims
        if v is True:
            prims.append(i)
    return prims
print(find_prime_2(100))
class hashtable(object):
    def __init__(self):
        self.hash_table = [[None, None] for i in range(10)]

    def hash(self, k, i):
        h_value = (k+i) % 10
        if self.hash_table[h_value][0] == k:
            return h_value
        if self.hash_table[h_value][0] != None:
            i = i+1#再探测
            h_value = self.hash(k, i)
        return h_value

    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]
a = hashtable()
a.put(13,26)
a.put(3,6)
a.get(3)
a.hash_table   
a.put(3,9)             
class hashtable(object):
    def __init__(self):
        self.hash_table = [[None, None] for i in range(10)]

    def hash(self, k, i):
        h_value = (k+i) % 10
        if self.hash_table[h_value][0] == k:
            return h_value
        if self.hash_table[h_value][0] != None:
            i = i+1
            h_value = self.hash(k, i)
        return h_value

    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


table = hashtable()
for i in range(9):
    table.put(i, i)
print(table.get(3))
print(table.hash_table)    
'mmp'.span()
         
import re
print(re.match('www', 'www.shiyanlou.com').group())  # 在起始位置匹配
print(re.match('com', 'www.shiyanlou.com'))         # 不在起始位置匹配                  
                
    
    
        