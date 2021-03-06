import random


class Graph():
    def __init__(self, name, directed=False):
        self.name = name
        self.nodes = {}
        self.edges = {}
        self.directed = directed

    def addNode(self, n):
        '''
        add a node to the graph; also add the appropriate edges
        '''
        if n.getName() not in self.nodes:
            self.nodes[n.getName()] = n
            self.addEdge(n)
            n.setGraph(self)
        return True

    def addEdge(self, n):
        '''
        add the appropriate edges for a given node
        if the graph is undirecte, don't add edge n1 -> n2 if edge n2 -> n1 exists
        '''
        neighbors = n.getNeighbors()
        if not neighbors:
            return False
        name = n.getName()
        for neighbor in neighbors:
            nbr = (name, neighbor)
            if not self.directed:
                rbn = (neighbor, name)
            else:
                rbn = None
            if nbr not in self.edges and rbn not in self.edges:
                self.edges[nbr] = n.neighbors[neighbor]
        return True

    def removeNode(self, n):
        '''
        remove a node; also remove the appropriate edges
        '''
        if n.getName() in self.nodes:
            self.pop(n.getName())
            self.removeEdge(n)
            n.unsetGraph()
        return True

    def removeEdge(self, n):
        '''
        remove each edge in self.edges that references a node that was removed
        '''
        for edge in self.edges:
            if n.getName() in edge:
                self.edges.pop(edge)
        return True

    def randomNode(self):
        '''
        return a random node; mostly used for testing search functions
        '''
        return random.choice(list(self.nodes.keys()))


def mergeGraph(graph1, graph2):
    newGraph = Graph(name="%s %s" %(graph1.name, graph2.name),
                directed=(graph1.directed and graph2.directed))
    if (not graph1.directed and not graph2.directed) or (graph1.directed and graph2.directed):
        newGraph.nodes = {**graph1.nodes, **graph2.nodes}
        newGraph.edges = {**graph1.edges, **graph2.edges}
    else:
        # have to implement this
        # for now just
        pass
    return newGraph
