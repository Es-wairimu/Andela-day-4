# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 07:16:30 2017

@author: nimselsa
"""

class BinarySearch(object):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alist = range(b, (a*b)+1, b)  
        self.length = a
        
    
    def __getitem__(self, c):
        return self.alist[c]
        
        
    def __setitem__(self, c, value):
        return self.alist[c] == value
        
    """Search method to find if the value is in the list"""
    
    def search(self, value):
        first_number = 0
        last_number = self.a - 1
        count = 0
        
        if self.alist[first_number] == value:
            return {'count': 0, 'index': first_number}
            
        if self.alist[last_number] == value:
            return {'count': 0, 'index': last_number}
            
       
        while first_number <= last_number:
            mid_point = (first_number + last_number) // 2
            count += 1
            
            if self.alist[mid_point] == value:
                return {'count': count, 'index': mid_point}
                
            elif value > self.alist[mid_point]:
                first_number = mid_point + 1
                
            elif value < self.alist[mid_point]:
                last_number = mid_point - 1
        
        if first_number > last_number :
            return {'count': 0, 'index': -1}