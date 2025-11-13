from typing import Any


from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current = frontier.pop()
        for neighbor in graph[current]:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return list(result)





def connected(graph):
    start_node = list(graph.keys())[0]
    reachable_nodes = reachable(graph, start_node)
    return len(reachable_nodes) == len(graph)


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    result = 0
    remaining_nodes = set(graph.keys())
    while len(remaining_nodes) > 0:
        start_node = remaining_nodes.pop()
        reachable_nodes = reachable(graph, start_node)
        result += 1
        remaining_nodes -= set(reachable_nodes)
    return result