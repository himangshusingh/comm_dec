# to generate graphs

from collections import defaultdict

graph = defaultdict(list)

# adding edges to the graph


def addedge(graph, u, v):
    graph[u].append(v)

# function

def generate_edges(graph):
    edges = []

    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


# graph as a dictionary

addedge(graph, 'a', 'c')
addedge(graph, 'b', 'c')
addedge(graph, 'b', 'e')
addedge(graph, 'c', 'd')
addedge(graph, 'c', 'e')
addedge(graph, 'c', 'a')
addedge(graph, 'c', 'b')
addedge(graph, 'e', 'b')
addedge(graph, 'd', 'c')
addedge(graph, 'e', 'c')


print(generate_edges(graph))
