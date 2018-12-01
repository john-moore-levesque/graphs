import graph
import node
import random
import string
import search


def testGraph(numnodes=40, directed=False, weighted=False):
    '''
    create a test graph called "Test Graph"
    by default it is an unweighted, undirected graph with 40 nodes
    '''
    def _createRandomNode():
        '''
        create a node with a random name
        '''
        name = ''.join([random.choice(string.ascii_letters) for _ in range(3)])
        return createNode(name)

    def _linkNodes(node1, node2, directed, weight):
        '''
        link two nodes together
        '''
        connectNodes(node1, node2, directed, weight)

    g = makeGraph("Test Graph", directed)
    nodes = [_createRandomNode() for n in range(numnodes)]
    maxedges = numnodes * (numnodes - 1)
    if not directed:
        maxedges //= 2
    numedges = random.randint(maxedges//10, maxedges)
    for edge in range(numedges):
        node1 = random.choice(nodes)
        node2 = random.choice(nodes)
        if weighted:
            weight = random.randint(0, 10)
        else:
            weight = None
        _linkNodes(node1, node2, directed, weight)
    for n in nodes:
        g.addNode(n)
    return g


def smallTest(directed=False, weighted=False):
    '''
    create a small test graph with 10 nodes
    '''
    return testGraph(10, directed, weighted)


def makeGraph(name, directed=False):
    '''
    make a new graph
    '''
    return graph.Graph(name, directed)


def createNode(name, data=None):
    '''
    make a new node
    '''
    return node.Node(name, data)


def connectNodes(node1, node2, directed=False, weight=None):
    '''
    connect two nodes together
    '''
    node1.addNeighbor(node2, directed, weight)
    if not directed:
        node2.addNeighbor(node1, directed, weight)
    return True


def testSearch(directed=False, weighted=False):
    '''
    test search on a small graph with 10 nodes
    by default the graph is undirected and unweighted
    '''
    g = smallTest(directed, weighted)
    while len(g.edges) < 20:
        g = smallTest()
    formatPath, searchFunctions = search.testSearcher(g)
    start = g.randomNode()
    end = g.randomNode()
    results = {}
    for key, value in searchFunctions.items():
        if "Destination" in key:
            results[key] = value(start, end)[0]
        else:
            results[key] = value(start)[0]
    for key, value in results.items():
        print("%s" %(key))
        print(formatPath(value))
        print("")
