from typing import List, Optional
from maze.util import Coordinates
from maze.graph import Graph


class IncMatGraph(Graph):
    """
    Incidence matrix implementation of an undirected graph, where each edge may or may not have a wall.
    """

    def __init__(self):
        super().__init__()
        self.vertices: List[Coordinates] = []
        self.edges: List[tuple[Coordinates, Coordinates, bool]] = []
        self.incidence_matrix: List[List[int]] = []

    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            self.vertices.append(label)
            # Add a new column to the incidence matrix for the new vertex
            for row in self.incidence_matrix:
                row.append(0)

    def addVertices(self, vertLabels: List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if self.hasVertex(vert1) and self.hasVertex(vert2):
            if not self.hasEdge(vert1, vert2):
                # Add the edge
                self.edges.append((vert1, vert2, addWall))
                # Add a row to the incidence matrix for this edge
                row = [0] * len(self.vertices)
                row[self.vertices.index(vert1)] = 1
                row[self.vertices.index(vert2)] = 1
                self.incidence_matrix.append(row)
                return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                # Remove edge and corresponding row from incidence matrix
                self.edges.pop(i)
                self.incidence_matrix.pop(i)
                return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for v1, v2, _ in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                # Update the wall status for the edge
                self.edges[i] = (v1, v2, wallStatus)
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
            vertex_index = self.vertices.index(label)
            for i, row in enumerate(self.incidence_matrix):
                if row[vertex_index] == 1:
                    edge = self.edges[i]
                    neighbour = edge[0] if edge[1] == label else edge[1]
                    neighbours.append(neighbour)
        return neighbours
