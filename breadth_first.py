#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 23:45:33 2018

@author: my-macbook
"""
from collections import deque

staff = {}
staff['Nick'] = ['Josh','Sam','Toby','Hugh','Michal']
staff['Sam'] = ['Oli','Elliot','Anna','Jas','Tom']
staff['Toby'] = ['Tash']
staff['Mark'] = ['Nick','Tim']
staff['Tim'] = []
staff['Tash'] = []
staff['Josh'] = []
staff['Hugh'] = []
staff['Michal'] = []
staff['Oli'] = []
staff['Elliot'] = []
staff['Anna'] = []
staff['Jas'] = []
staff['Tom'] = []

def is_person_seller(p):
    '''
    input: name string
    output: T if name ends in 'm' else F
    '''
    return p[-1] == 'a'
    
def find_s(g):
    '''
    input: graph as dictionary
    output: anyone who's name ends in 'm'
    '''
    search_queue = deque()
    search_queue += staff['Mark']
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_person_seller(person):
                return 'We found a seller: ' + person
            else:
                search_queue += staff[person]
                searched.append(person)
    return False
            
find_s(staff)