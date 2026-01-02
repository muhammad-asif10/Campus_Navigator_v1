from core.dijkstra import dijkstra

def find_shortest_path(graph, start, end):
    if start not in graph.adjacency_list or end not in graph.adjacency_list:
        return None, float('inf')

    distances, previous = dijkstra(graph, start)

    if end not in distances or distances[end] == float('inf'):
        return None, float('inf')

    path = []
    current = end

    while current is not None:
        path.insert(0, current)
        current = previous.get(current)

    if path and path[0] == start:
        return path, distances[end]

    return None, float('inf')
