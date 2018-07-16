#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 08:59:25 2018

@author: my-macbook
"""

N = 3

for i in range(2**N):
    for j in range(N):
            # test bit jth of integer i
            print('i: ' + str(i))
            print('j: ' + str(j))
            print('i >> j: ' + str(i >> j))
            print('i << j: ' + str(i << j))
    