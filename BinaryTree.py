# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:16:27 2020

@author: vais4
"""

class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def addChild(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)
                
    def traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.traversal()
            
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
               return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
               return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self
            
if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34,-4,17]
    
    root = BinaryTree(numbers[0])
    
    for i in range (1,len(numbers)): 
        root.addChild(numbers[i])
        
    print(root.traversal())
    print(root.search(21))
    root.delete(9)
    print(root.traversal())
            
        
        