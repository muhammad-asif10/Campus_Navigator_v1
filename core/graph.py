class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def _ensure_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, source, destination, weight):
        self._ensure_node(source)
        self._ensure_node(destination)

        self._upsert_edge(source, destination, weight)
        self._upsert_edge(destination, source, weight)

    def _upsert_edge(self, source, destination, weight):
        for index, (neighbor, existing_weight) in enumerate(self.adjacency_list[source]):
            if neighbor == destination:
                if weight < existing_weight:
                    self.adjacency_list[source][index] = (destination, weight)
                return

        self.adjacency_list[source].append((destination, weight))

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def get_neigbours(self, node):
        return self.get_neighbors(node)
