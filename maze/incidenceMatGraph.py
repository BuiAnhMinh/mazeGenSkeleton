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
        self.vertices: Dict[Coordinates, int] = {}  # Maps vertex to its index in the matrix
        self.edges: List[Tuple[Coordinates, Coordinates, bool]] = []
        self.incidence_matrix: List[Dict[int, int]] = []  # Sparse representation

    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            index = len(self.vertices)
            self.vertices[label] = index
            self.incidence_matrix.append({})

    def addVertices(self, vertLabels: List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if self.hasVertex(vert1) and self.hasVertex(vert2):
            if not self.hasEdge(vert1, vert2):
                # Add the edge
                self.edges.append((vert1, vert2, addWall))
                # Update the incidence matrix with the edge connection
                idx1 = self.vertices[vert1]
                idx2 = self.vertices[vert2]
                self.incidence_matrix[idx1][len(self.edges) - 1] = 1
                self.incidence_matrix[idx2][len(self.edges) - 1] = 1
                return True
        return False
    
    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                # Update the wall status for the edge
                self.edges[i] = (v1, v2, wallStatus)
                return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                # Remove edge from list and incidence matrix
                self.edges.pop(i)
                self._remove_from_incidence_matrix(i)
                return True
        return False

    def _remove_from_incidence_matrix(self, edge_index: int):
        for matrix_row in self.incidence_matrix:
            if edge_index in matrix_row:
                del matrix_row[edge_index]

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        idx1 = self.vertices.get(vert1)
        idx2 = self.vertices.get(vert2)
        if idx1 is not None and idx2 is not None:
            for edge_index in self.incidence_matrix[idx1]:
                if edge_index in self.incidence_matrix[idx2]:
                    return True
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> Optional[bool]:
        for v1, v2, wallStatus in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return wallStatus
        return None

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        neighbours = []
        if self.hasVertex(label):
            vertex_index = self.vertices[label]
            for edge_index in self.incidence_matrix[vertex_index]:
                edge = self.edges[edge_index]
                neighbour = edge[0] if edge[1] == label else edge[1]
                neighbours.append(neighbour)
        return neighbours
