# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


import time
from typing import List, Dict, Tuple, Optional

from maze.util import Coordinates
from maze.graph import Graph


class IncMatGraph(Graph):
    """
    Incidence matrix implementation of an undirected graph with optimized runtime,
    where each edge may or may not have a wall.
    """

    def __init__(self):
        super().__init__()
        self.vertices: Dict[Coordinates, int] = {}  # map vertex with index
        self.edges: List[Tuple[Coordinates, Coordinates, bool]] = [] #edge with wall status
        self.incidence_matrix: List[Dict[int, int]] = []  # sparse representation https://www.geeksforgeeks.org/sparse-matrix-representation/, reduce run time

    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            index = len(self.vertices) #get next index
            self.vertices[label] = index #map vertex to this index 
            self.incidence_matrix.append({}) #add a new row 

    def addVertices(self, vertLabels: List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if self.hasVertex(vert1) and self.hasVertex(vert2): #check both vertices exist
            if not self.hasEdge(vert1, vert2): #check edge exist 
                self.edges.append((vert1, vert2, addWall)) #add new edge
                #update matrix 
                idx1 = self.vertices[vert1] 
                idx2 = self.vertices[vert2]
                self.incidence_matrix[idx1][len(self.edges) - 1] = 1
                self.incidence_matrix[idx2][len(self.edges) - 1] = 1
                return True
        return False
    
    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        for i, (v1, v2, _) in enumerate(self.edges): #check edge exist 
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                #update wall status 
                self.edges[i] = (v1, v2, wallStatus)
                return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for i, (v1, v2, _) in enumerate(self.edges):
            #check edge exist 
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                #remove edge 
                self.edges.pop(i)
                self._remove_from_incidence_matrix(i) #update matrix 
                return True
        return False

    def _remove_from_incidence_matrix(self, edge_index: int):
        for matrix_row in self.incidence_matrix:
            if edge_index in matrix_row:
                del matrix_row[edge_index] #remove edge index 

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        idx1 = self.vertices.get(vert1) #get index 1st vertex
        idx2 = self.vertices.get(vert2) #get index 2nd vertex
        if idx1 is not None and idx2 is not None:
            # check for shared edge
            for edge_index in self.incidence_matrix[idx1]:
                if edge_index in self.incidence_matrix[idx2]:
                    return True
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> Optional[bool]:
        for v1, v2, wallStatus in self.edges:
            # check edge exist 
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return wallStatus
        return None

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        neighbours = []
        if self.hasVertex(label): #check vertex exist 
            vertex_index = self.vertices[label] #get index 
            # loop edges in matrix for vertex 
            for edge_index in self.incidence_matrix[vertex_index]:
                edge = self.edges[edge_index] #get edge detail 
                #get neighbours of vertex 
                neighbour = edge[0] if edge[1] == label else edge[1]
                neighbours.append(neighbour)
        return neighbours
