import edge


class Node():
    def __init__(self, name, data=None):
        self.name = name
        self.neighbors = {}
        self.data = data

    def hasNeighbor(self, node):
        '''
        if the supplied node is a neighbor of self, return True; else return False
        '''
        if node.name not in self.neighbors:
            return False
        return True

    def addNeighbor(self, node, directed, weight):
        '''
        if a given node is not already a neighbor, add it
        if the graph is not directed, make self a neighbor of node
        '''
        if not self.hasNeighbor(node):
            _edge = edge.Edge(self, node, directed, weight)
            self.neighbors[node.name] = _edge
            if not directed:
                node.addNeighbor(self, directed, weight)
        return True

    def removeNeighbor(self, node, directed):
        '''
        remove a given node from the neighbors dict
        if the graph is not directed, remove self from the neighbors dict of the given
            node
        '''
        if self.hasNeighbor(node):
            self.neighbors.pop(node.name)
            if not directed:
                node.removeNeighbor(self, directed)
        return True

    def getData(self):
        '''
        return the data field
        '''
        return self.data

    def setData(self, data):
        '''
        set the data field
        '''
        self.data = data

    def getNeighbors(self):
        '''
        return the neighbors dict
        '''
        return self.neighbors

    def getName(self):
        '''
        return the node name
        '''
        return self.name
