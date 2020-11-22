# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 01:18:48 2020

@author: vais4
"""

class Graph():
    def __init__(self,edges):
        self.edges = edges
        
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def all_routes(self, start, end, path= []):
        path = path + [start]        
        
        if start ==  end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        all_possible_paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.all_routes(node, end, path)
                for p in new_path:
                    all_possible_paths.append(p)                                  
        
        return all_possible_paths
    
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortestpath = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortestpath is None or len(sp) < len(shortestpath):
                        shortestpath = sp
                        
        return shortestpath             


if __name__ == "__main__":
    routes = [('Mumbai','Paris'),
              ('Mumbai','Dubai'),
              ('Paris','Dubai'),
              ('Paris','New York'),
              ('Dubai','New York'),
              ('New York','Toronto'),
              ('Mumbai','Amsterdam')]
    
    routes_graph = Graph(routes)
    
    all_paths = routes_graph.all_routes('Mumbai','New York')
    print("All routes are ", all_paths)
        
    shortest_path = routes_graph.get_shortest_path('Mumbai','New York')
    print("Shortest route is ", shortest_path)