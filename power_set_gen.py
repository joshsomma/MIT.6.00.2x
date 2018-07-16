#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 08:51:11 2018

@author: my-macbook
"""

items = ['red','green','blue']

'''
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
'''

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        bags = ([],[])
        for j in range(N):
            #print('i =', i, '; j =', j, ';; i // 3**j =', i //3**j)
            if (i // 3**j) % 3 == 1:
                bags[0].append(items[j])
            elif (i // 3**j) % 3 == 2:
                bags[1].append(items[j])
        yield bags
        
yieldAllCombos(items)