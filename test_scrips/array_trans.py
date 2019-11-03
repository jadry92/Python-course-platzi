#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:08:44 2017

@author: sebastian
"""
import numpy as np

n1=100
n2=200
n3=300

array_ini = np.random.random([n1,n2,n3])
array_out_1 = np.zeros([n1,n2])

print(array_ini[0][0][2])
for i in range(0,n3):
    array_out_1[:][:] = array_out_1[:][:] + array_ini[:][:][i]
