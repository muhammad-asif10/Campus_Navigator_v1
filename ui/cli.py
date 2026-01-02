def run_cli(graph):
    print("\nAvailable locations:")
    for location in graph.adjacency_list.keys():
        print("-", location)

    start = input("Enter current location: ").strip()
    end = input("Enter destination: ").strip()

    return start, end
