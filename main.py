import networkx as nx
import matplotlib.pyplot as plt
import sys


def minDistance(dist, mstSet, V):
    min = sys.maxsize  # assigning largest numeric value to min
    for v in range(V):
        if mstSet[v] == False and dist[v] < min:
            min = dist[v]
            min_index = v
    return min_index


def prims(G, pos):
    V = len(G.nodes())  # V denotes the number of vertices in G
    dist = []  # dist[i] will hold the minimum weight edge value of node i to be included in MST
    parent = [None] * V  # parent[i] will hold the vertex connected to i, in the MST edge
    mstSet = []  # mstSet[i] will hold true if vertex i is included in the MST
    # initially, for every node, dist[] is set to maximum value and mstSet[] is set to False
    for i in range(V):
        dist.append(sys.maxsize)
        mstSet.append(False)
    dist[0] = 0
    parent[0] = -1  # starting vertex is itself the root, and hence has no parent
    for count in range(V - 1):
        u = minDistance(dist, mstSet, V)  # pick the minimum distance vertex from the set of vertices
        mstSet[u] = True
        # update the vertices adjacent to the picked vertex
        for v in range(V):
            if (u, v) in G.edges():
                if mstSet[v] == False and G[u][v]['length'] < dist[v]:
                    dist[v] = G[u][v]['length']
                    parent[v] = u
    for X in range(V):
        if parent[X] != -1:  # ignore the parent of the starting node
            if (parent[X], X) in G.edges():
                nx.draw_networkx_edges(G, pos, edgelist=[(parent[X], X)], width=2.5, alpha=0.6, edge_color='r')
    return


def DrawGraph(G):
    pos = nx.spring_layout(G)
    print(pos)
    nx.draw(G, pos, with_labels=True)  # with_labels=true is to show the node number in the output graph
    edge_labels = nx.get_edge_attributes(G, 'length')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=11)  # prints weight on all the edges
    return pos


def CreateGraph():
    G = nx.Graph()
    nodes = []
    X = []
    Y = []
    with open('benchmark/input10.txt') as input_data:
        str(input_data.readline())
        str(input_data.readline())
        n = int(input_data.readline())
        print(n)
        str(input_data.readline())

        for line in input_data:
            if len(line.split()) == 0:
                break
            elif len(line.split()) == 3:
                n, x, y = line.split()
                nodes.append(n)
                X.append(float(x))
                Y.append(float(y))
                G.add_node(n, pos=(x, y))

        for line in input_data:
            if len(line.split()) == 0:
                continue
            elif len(line.split()) == 1:
                start = line.split().pop(0)
                print(start)
            else:
                edgeInfo = line.split()
                edgeFrom = edgeInfo.pop(0)
                # print(edgeFrom)
                # print(edgeInfo)
                while len(edgeInfo) > 0:
                    edgeTo = edgeInfo[0]
                    edgeCost = edgeInfo[2]
                    del edgeInfo[:4]
                    print(edgeFrom + "-" + edgeTo + " : " + edgeCost)
                    G.add_edge(edgeFrom, edgeTo, cost=edgeCost)

        # a, b = input_data.readline().split()
        # print(a)
        # print(b)
    print(nodes)
    print(X)
    print(Y)
    return G


# wtMatrix = []
# for i in range(n):
#     list1 = map(int, (f.readline()).split())
#     wtMatrix.append(list1)
# # Adds edges along with their weights to the graph
# for i in range(n):
#     for j in range(n)[i:]:
#         if wtMatrix[i][j] > 0:
#             G.add_edge(i, j, length=wtMatrix[i][j])
# return G


if __name__ == "__main__":
    G = CreateGraph()
    pos = nx.get_node_attributes(G, 'pos')
    print(pos)
    plt.axis(True)
    plt.tick_params(axis='both')
    DrawGraph(G)
    plt.show()
