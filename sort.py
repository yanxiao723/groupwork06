# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:11:55 2020

@author: yan
"""

#bubble_sort
def bubble_sort(seq):
    size = len(seq)
    for i in range(1,size):
        for j in range(0,size-1):
            if seq[j] > seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
    return seq
def choose_sort(seq):
    size = len(seq)
    for i in range(size-1):
        minv = i
        for j in range(i+1,size):
            if seq[j]< seq[minv]:
                minv = j
        seq[minv],seq[i] = seq[i],seq[minv]
    return seq
def insert_sort(seq):
    size = len(seq)
    for i in range(size):
        index = i 
        while index > 0 and seq[index] < seq[index-1]:
            seq[index],seq[index-1] = seq[index-1],seq[index]
            index -=1#从后往前遍历比较
    return seq
def merge_sort(seq):
    if(len(seq) < 2):
        return seq
    size = len(seq)
    mid = size//2
    left,right = seq[:mid],seq[mid:]
    def merge(left,right):
        result =[]
        while left and  right:
            if left[0]<=right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while  left:
                result.append(left.pop(0))
        while  right:
                result.append(right.pop(0))
        return result
    return merge(merge_sort(left),merge_sort(right))
def quick_sort(seq):#快速排序1
    if len(seq)<2:
        return seq
    else:
        pivot = seq[0]
        left = [i for i in seq[1:] if i<=pivot]
        right = [ i for i in seq[1:] if i>pivot]
    return quick_sort(left) + [pivot] +quick_sort(right)
def quick_select(sequence):#快速排序2
    def recursive(begin, end):
        if begin > end:
            return
        left, right = begin, end
        pivot = sequence[left]
        while left < right:
            while left < right and sequence[right] > pivot:
                right = right-1
            while left < right and sequence[left] <= pivot:
                left = left+1
            sequence[left], sequence[right] = sequence[right], sequence[left]
        sequence[left], sequence[begin] = sequence[begin], sequence[left]
        recursive(begin, left - 1)
        recursive(right + 1, end)

    recursive(0, len(sequence) - 1)
    return sequence

            
            
            
        
    
    
list1=[12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
choose_sort(list1)
bubble_sort(list1)
insert_sort(list1)
merge_sort(list1)
quick_sort(list1)
quick_select(list1)
list(range(0,5,5))