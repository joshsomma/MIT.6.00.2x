#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:33:25 2018

@author: my-macbook
"""

class Food(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'
    
def buildMenu(names, values, calories):
    """
    names, values, calories all lists of the same length
    names - a list of strings
    values and calories lists of numbers
    returns - list of foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(names[i], values[i], calories[i])
    return menu

def greedy(items, maxCost, keyFunction):
    # sorted() is different than sort(); sorted() returns a new sorted list; sort() sorts an existing list
    items_copy = sorted(items, key=keyFunction, reverse=True)
    
    result =[]
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(items_copy)):
        if (totalCost + items_copy[i].getCost()) <= maxCost:
            result.append(items_copy[i])
            totalCost += items_copy[i].getCost()
            totalValue += items_copy[i].getValue()
            
    # O(n log n)
    return (result, totalValue)
            
    