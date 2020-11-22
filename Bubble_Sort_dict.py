# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:30:12 2020

@author: vais4
"""

def bubble_sort(elements,key):
    size = len(elements)
        
    for i in range(size-1):
        swaped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]: 
                tmp = elements[j+1]
                elements[j+1] = elements[j]
                elements[j] = tmp
                swaped = True
            
        if not swaped:
            break

if __name__ == '__main__':
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'reena', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'tina', 'transaction_amount': 200, 'device': 'one plus 8t'},
        {'name': 'raina', 'transaction_amount': 800, 'device': 'iphone-8'},
        ]
    
    bubble_sort(elements,'transaction_amount')
    print(elements)