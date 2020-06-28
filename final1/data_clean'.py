#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:47:06 2020

@author: Fan Delin
__StudentID__=320180939721
__Group__=6
"""

import numpy as np

# the type of row_list should be the list of lists.
def data_cleaning(row_list: list):
    midd_list = []
    hours = len(row_list[0])
    for i in range(hours):
        mid_list = []#put the variable in ith row into the mid_list
        for j in range(len(row_list)):
            mid_list.append(row_list[j][i])
        midd_list.append(mid_list)#contribute mid_list to midd_list
    mean_value = []
    for i in midd_list:#Remove the maximum and minimum values in the list
        while np.var(i) > 100:
            i.remove(max(i))
            i.remove(min(i))
        else:
            mean_value.append(np.mean(i))
    return mean_value