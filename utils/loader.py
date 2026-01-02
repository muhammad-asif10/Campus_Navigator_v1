import json
from core.graph import Graph

def load_campus_map(file_path):
    graph = Graph()

    with open(file_path, 'r') as file:
        data = json.load(file)

    for source, neighbors in data.items():
        for destination, weight in neighbors.items():
            graph.add_edge(source, destination, weight)

    return graph
