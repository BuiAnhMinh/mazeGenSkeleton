# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class EdgeListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        ### Implement me! ###
<<<<<<< HEAD
        self.verticesList = {} 
    

=======
        self.vertices_dict:dict[list]={}
        self.edge_list:dict[tuple:bool]={}
>>>>>>> 7aafc89fc68daea6c4a4f6e12c2283212de67cf5

        
    def addVertex(self, label:Coordinates):
        ### Implement me! ###
<<<<<<< HEAD
        self.verticesList[len(self) + 1] = Coordinates
        


=======
        self.vertices_dict[label]=[]
        
   
>>>>>>> 7aafc89fc68daea6c4a4f6e12c2283212de67cf5

    def addVertices(self, vertLabels:List[Coordinates]):
        
        for vertex in vertLabels :
            self.addVertex(vertex)
        return (len(self.verticesList))
        ### Implement me! ###
<<<<<<< HEAD
        # for i in range (len(vertLabels)):
        #     self.addVertex(i) 

=======
        for vertex in vertLabels:
            self.addVertex(vertex)
   
>>>>>>> 7aafc89fc68daea6c4a4f6e12c2283212de67cf5


    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        
<<<<<<< HEAD
=======
        if not self.hasEdge(vert1, vert2):
            self.edge_list[(vert1, vert2)] = addWall
            self.edge_list[(vert2, vert1)] = addWall
            self.vertices_dict[vert1].append(vert2)
            self.vertices_dict[vert2].append(vert1)
            return True
        else:
            return False
   
     
>>>>>>> 7aafc89fc68daea6c4a4f6e12c2283212de67cf5
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        if self.hasEdge(vert1, vert2):
            self.edge_list[(vert1, vert2)] = wallStatus
            self.edge_list[(vert2, vert1)] = wallStatus
            return True
        return False
        
        
    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if self.hasEdge(vert1, vert2):
            self.vertices_dict[vert1].remove(vert2)
            self.vertices_dict[vert2].remove(vert1)
            del self.edge_list[(vert1, vert2)]
            del self.edge_list[(vert2, vert1)]
            return True


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if label in self.vertices_dict.keys():
            return True
        return False




    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if (vert1, vert2) in self.edge_list.keys():
                return True
        return False

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return self.edge_list[(vert1, vert2)]
        
    
    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        # remember to return list of coordinates
        return self.vertices_dict[label]
        