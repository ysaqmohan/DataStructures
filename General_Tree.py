# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:01:56 2020

@author: vais4
"""

class Tree():
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None        
     
    def addNode(self,node):
        node.parent = self 
        self.children.append(node)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
            
        return level
        
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix , self.data)
        
        for child in self.children:
            if self.children: 
                child.print_tree()
        
if __name__ == '__main__':
    MovieCrew = Tree("MovieCrew")    
    
    Actors =  Tree("Actors")
    MovieCrew.addNode(Actors) 
    
    Directors = Tree("Directors")
    MovieCrew.addNode(Directors)
    
    StoryWriters = Tree("StoryWriters")
    MovieCrew.addNode(StoryWriters)
    
    Actors.addNode(Tree("Cate Blanchett"))
    Actors.addNode(Tree("Leonardo DiCaprio"))
    Actors.addNode(Tree("Ryan Gosling"))
    Actors.addNode(Tree("Zoe Saldana"))
    
    Directors.addNode(Tree("Woodey Allen"))
    Directors.addNode(Tree("Christopher Nolan"))
    
    StoryWriters.addNode(Tree("Mario Puzo"))
    StoryWriters.addNode(Tree("Hommer"))
    
    MovieCrew.print_tree()
    
    
    
    
    

    