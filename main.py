from utils.loader import load_campus_map
from services.navigator import find_shortest_path
from ui.cli import run_cli

def main():
    graph = load_campus_map("data/campus_map.json")

    start, end = run_cli(graph)

    path, time = find_shortest_path(graph, start, end)

    if path:
        print("\nShortest path:")
        print(" -> ".join(path))
        print(f"Estimated time: {time} minutes")
    else:
        print("\nNo path found")

if __name__ == "__main__":
    main()