# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:21:03 2017

@author: nimselsa
"""

def find_missing(list1, list2):
    
    try:
        if isinstance(list1, list) and isinstance(list2, list):
            if list1 == [] and list2 == []:
                return 0
            else:
                
                set_a = set(list1)
                set_b = set(list2)
                list_new = set_a ^ set_b 
               
                if list_new == set():
                    return 0
                return int(list(list_new)[0]) 
    except ValueError():
        return 'Lists only'
  
     
