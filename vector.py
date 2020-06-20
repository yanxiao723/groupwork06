# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:19:25 2020

@author: yan
"""
import math
class Vector:
    def __init__(self,components=[]):
        self.__components = list(components)
    def set(self,components):
        if len(components) >0:
            self.__components = list(components)
        else:
            raise Exception('please give any vector')
    def __str__(self):
        #print(list(map(str,self.__components)))
        return '('+','.join(map(str,self.__components))+')'
#a = Vector([1,2,3])
#print(type(a))
#a = Vector([1,2])
#print(a)
#a.set([1])
#print(a)
#._Vector__components  获得私有变量值的方法 
#import numpy as np        
#type(np.array([1]))     
    def __len__(self):
        return len(self.__components)
    def eulidlength(self):
        sum1 = 0
        for i in self.__components:
            sum1+=i**2
        return math.sqrt(sum1)
    def component(self,i):
        if type(i) is int and -len(self.__components)<=i <len(self.__components):
            return self.__components[i]
        else:
            raise Exception('index out of range')    
#a = Vector([1,2,3])
#a.component(0)
    def changeComponent(self,pos,value):
        assert (-len(self.__components)<=pos <len(self.__components))
        self.__components [pos] = value
#a = Vector([1,2,3])
#a.changeComponent(6,2)
    def __add__(self,other):
        size = len(self)
        if size == len(other):
            result = [other[i]+self.__components[i] for i in range(size)]
            return Vector(result)
        else:
            raise Exception('must have the same size')
    def __sub__(self,other):
        size = len(self)
        if size == len(other):
            result = [-other[i]+self.__components[i] for i in range(size)]
            return Vector(result)
        else:
            raise Exception('must have the same size')
    def __mul__(self,other):
        size = len(self)
        if isinstance(other,float) or isinstance(other,int):
            ans = [i*other for i in self.__components ]
            return ans
        elif (isinstance(other,Vector)) and (len(other) == len(self)):
            size =len(self)
            sum1 =0
            for i in range(size):
                sum1+=self.__components[i]*other.component(i)
        else:
            raise Exception('invalid operand')
def zeroVector(demension):
    assert (isinstance(demension,int))
    return Vector([0]*demension)
def unitBasisVector(dimension, pos):  # 单位基向量的实现
    assert(isinstance(dimension, int) and (isinstance(pos, int)))
    ans = [0]*dimension
    ans[pos] = 1
    return Vector(ans)
#a = unitBasisVector(3,5)
#a._Vector__components
            
        
        