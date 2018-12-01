class Searcher():
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph

    def depthFirstSearch(self, start=None):
        '''
        do depth-first search; if no start node supplied a random node is used
        '''
        def _dfs(node, marked=[], explored=[]):
            marked.append(node)
            n = self.graph.nodes[node]
            for neighbor in n.getNeighbors():
                if neighbor not in explored:
                    if neighbor not in marked:
                        explored.append(neighbor)
                        _dfs(neighbor, marked, explored)
            return marked, explored

        if not start or start not in self.graph.nodes:
            start = self.graph.randomNode()

        return _dfs(start)

    def breadthFirstSearch(self, start=None):
        '''
        do a breadth-first search; if no start node supplied, a random node is used
        '''
        def _bfs(node):
            queue = [node]
            marked = [node]
            explored = []
            while queue:
                curr = queue.pop()
                n = self.graph.nodes[curr]
                for neighbor in n.getNeighbors():
                    if neighbor not in marked:
                        marked.append(neighbor)
                        explored.append(neighbor)
                        queue.append(neighbor)
            return marked, explored

        if not start or start not in self.graph.nodes:
            start = self.graph.randomNode()

        return _bfs(start)

    def depthFirstSearchDest(self, start=None, end=None):
        '''
        do depth-first search, looking for a path between two nodes
        if neither a start node or an end node are not supplied, random nodes
            are used for each
        '''
        def _dfsd(node, end, marked=[], explored=[]):
            marked.append(node)
            n = self.graph.nodes[node]
            if end in n.getNeighbors():
                marked.append(end)
                explored.append(node)
                explored.append(end)
                return marked, explored
            for neighbor in n.getNeighbors():
                if neighbor not in explored:
                    if neighbor not in marked:
                        explored.append(neighbor)
                        _dfsd(neighbor, end, marked, explored)
            return None, None

        if not start or start not in self.graph.nodes:
            start = self.graph.randomNode()
        if not end or end not in self.graph.nodes:
            end = self.graph.randomNode()

        return _dfsd(start, end)

    def breadthFirstSearchDest(self, start=None, end=None):
        '''
        do breadth-first search, looking for a path between two nodes
        if neither a start node or an end node are not supplied, random nodes
            are used for each
        '''
        def _bfsd(node, end):
            queue = [node]
            marked = [node]
            explored = []
            while queue:
                curr = queue.pop()
                n = self.graph.nodes[curr]
                for neighbor in n.getNeighbors():
                    if neighbor not in marked:
                        marked.append(neighbor)
                        explored.append(neighbor)
                        if neighbor == end:
                            return marked, explored
                        queue.append(neighbor)
            return None

        if not start or start not in self.graph.nodes:
            start = self.graph.randomNode()
        if not end or end not in self.graph.nodes:
            end = self.graph.randomNode()

        return _bfsd(start, end)

    def formatPath(self, path):
        '''
        format a path between nodes
        '''
        if isinstance(path, type(None)):
            return "No path found"
        formatted = []
        for p in path:
            formatted.append(p)
            formatted.append('--->')
        return ' '.join(formatted[:-1])


def testSearcher(graph):
    '''
    create a Searcher called "Test"
    return the formatPath method and also a dictionary of the various
        search methods
    '''
    test = Searcher("Test", graph)
    return test.formatPath, {"Depth-First Search": test.depthFirstSearch,
            "Depth-First Search (Destination)": test.depthFirstSearchDest,
            "Breadth-First Search": test.breadthFirstSearch,
            "Breadth-First Search (Destination)": test.breadthFirstSearchDest}
