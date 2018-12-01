class Edge():
    def __init__(self, start, end, directed=False, weight=None):
        self.start = start
        self.end = end
        self.directed = directed
        self.weight = weight
        self.name = (start.name, end.name)

    def getEndpoints(self):
        '''
        get endpoints for an edge
        note that the edge name is made up of the "name" field for the start ane end
            nodes; this method returns the actual nodes
        '''
        return self.start, self.end

    def getDirected(self):
        '''
        is the edge directed?
        '''
        return self.directed

    def getWeight(self):
        '''
        what is the weight of the edge?
        '''
        return self.weight
