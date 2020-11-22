# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:36:18 2020

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
        print(prefix , self.data[0], "(", self.data[1], ")")
        
        for child in self.children:
            if self.children: 
                child.print_tree()
                
if __name__ == '__main__':
    CEO = Tree(["Roger" , "CEO"])
    
    CTO = Tree(["Abraham", "CTO"])
    CEO.addNode(CTO)
    
    HR_Head = Tree(["Benjamin", "HR Head"])
    CEO.addNode(HR_Head)
    
    Infrastructure_head = Tree(["Chris" , "Infrastructure Head"])
    CTO.addNode(Infrastructure_head)
    
    App_Manager =  Tree(["Liam", "App Manager"])
    Infrastructure_head.addNode(App_Manager)
    
    Cloud_Manager = Tree(["Barry", "Cloud Manager"])
    Infrastructure_head.addNode(Cloud_Manager)
    
    Application_Head = Tree(["Clark", "Application Head"])
    CTO.addNode(Application_Head)
    
    Recruitment_Manager = Tree(["Alfred", "Recruitment Manager"])
    HR_Head.addNode(Recruitment_Manager)
    
    Policy_Manager = Tree(["Bruce", "Policy Manager"])
    HR_Head.addNode(Policy_Manager)
    
    CEO.print_tree()