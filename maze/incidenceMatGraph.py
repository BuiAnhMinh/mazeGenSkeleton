from typing import List, Optional
from maze.util import Coordinates
from maze.graph import Graph


class IncMatGraph(Graph):
    """
    Represents an undirected graph using an incidence matrix.
    """

    def __init__(self):
        # Initialize vertices and incidence matrix
        self.vertices: List[Coordinates] = []
        self.edges: List[tuple] = []
        self.incidence_matrix: List[List[int]] = []

    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            self.vertices.append(label)
            # Add a new column to the incidence matrix for the new vertex
            for row in self.incidence_matrix:
                row.append(0)

    def addVertices(self, vertLabels: List[Coordinates]):
        for vertex in vertLabels:
            self.addVertex(vertex)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if not self.hasEdge(vert1, vert2):
            if vert1 in self.vertices and vert2 in self.vertices:
                # Add new edge with wall status
                edge = (vert1, vert2, addWall)
                self.edges.append(edge)
                # Add a new row for this edge in the incidence matrix
                row = [0] * len(self.vertices)
                row[self.vertices.index(vert1)] = 1
                row[self.vertices.index(vert2)] = 1
                self.incidence_matrix.append(row)
                return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        # Find the index of the edge in the edges list
        edge_index = self._find_edge_index(vert1, vert2)
        if edge_index is not None:
            # Update the wall status in the corresponding edge tuple
            vert1, vert2, _ = self.edges[edge_index]
            self.edges[edge_index] = (vert1, vert2, wallStatus)
            return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        edge_index = self._find_edge_index(vert1, vert2)
        if edge_index is not None:
            # Remove the edge from the list and the corresponding row from the matrix
            self.edges.pop(edge_index)
            self.incidence_matrix.pop(edge_index)
            return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        return self._find_edge_index(vert1, vert2) is not None

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> Optional[bool]:
        edge_index = self._find_edge_index(vert1, vert2)
        if edge_index is not None:
            return self.edges[edge_index][2]
        return None

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        neighbours = []
        if label in self.vertices:
            index = self.vertices.index(label)
            for i, row in enumerate(self.incidence_matrix):
                if row[index] == 1:
                    edge = self.edges[i]
                    neighbour = edge[0] if edge[1] == label else edge[1]
                    neighbours.append(neighbour)
        return neighbours

    def _find_edge_index(self, vert1: Coordinates, vert2: Coordinates) -> Optional[int]:
        for i, edge in enumerate(self.edges):
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                return i
        return None
