# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


import time
from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class EdgeListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.vertices_dict:dict[list]={} #dictionary to store edges
        self.edge_list:dict[tuple:bool]={} #add wall status 

    def addVertex(self, label:Coordinates):
        self.vertices_dict[label]=[] #initialize an empty list 
        
    def addVertices(self, vertLabels:List[Coordinates]):
        for vertex in vertLabels: #loop vertices list 
            self.addVertex(vertex) #add vertex using addVertex()
   
    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        if not self.hasEdge(vert1, vert2): #check edge exist 
            self.edge_list[(vert1, vert2)] = addWall #add edge with wall status 
            self.edge_list[(vert2, vert1)] = addWall #add reverse edge (undirected graph)
            self.vertices_dict[vert1].append(vert2) #add vert2
            self.vertices_dict[vert2].append(vert1) #add vert1 
            return True #add edge 
        else:
            return False #edge already exist 

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        if self.hasEdge(vert1, vert2): #check edge exist
            self.edge_list[(vert1, vert2)] = wallStatus #update wall status of edge
            self.edge_list[(vert2, vert1)] = wallStatus #update wall status of reverse edge
            return True #update wall status success
        return False # edge not exist 
        
    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.hasEdge(vert1, vert2): #check edge exist 
            self.vertices_dict[vert1].remove(vert2) #remove vert2 from adjecency list of vert1
            self.vertices_dict[vert2].remove(vert1) #remove vert1 from adjecency list of vert2 
            del self.edge_list[(vert1, vert2)] #delete edge 
            del self.edge_list[(vert2, vert1)] #delete reverse edge 
            return True #edge removed 
        return False #edge not exist

    def hasVertex(self, label:Coordinates)->bool:
        if label in self.vertices_dict.keys(): #check vertex exist 
            return True #vertex exist
        return False #vertex not exist 

    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if (vert1, vert2) in self.edge_list.keys(): #check edge exist 
                return True #edge exist
        return False #edge not exist 

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        return self.edge_list[(vert1, vert2)] #get wall status between vert1 and vert2
            
    def neighbours(self, label:Coordinates)->List[Coordinates]:
        return self.vertices_dict[label] #return list of adjacency vertices 
    
        