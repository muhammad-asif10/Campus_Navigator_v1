# Campus Navigator

A Python-based command-line application that helps users navigate the campus by finding the shortest path between two locations. This project demonstrates the application of Data Structures and Algorithms, specifically Graph theory and Dijkstra's algorithm.

## Features

- **Interactive CLI**: Simple command-line interface to select start and destination points.
- **Shortest Path Calculation**: Uses Dijkstra's algorithm to find the most efficient route.
- **Time Estimation**: Calculates the estimated time to travel between locations based on edge weights.
- **Data-Driven**: Loads campus map data from a JSON file, making it easy to update locations and connections.

## Project Structure

```
Campus_Navigator/
├── core/               # Core data structures and algorithms
│   ├── dijkstra.py     # Implementation of Dijkstra's algorithm
│   └── graph.py        # Graph data structure implementation
├── data/               # Data files
│   └── campus_map.json # JSON file containing campus locations and connections
├── services/           # Business logic
│   └── navigator.py    # Service to coordinate pathfinding
├── ui/                 # User Interface
│   └── cli.py          # Command-line interface handler
├── utils/              # Utility functions
│   └── loader.py       # JSON data loader
├── main.py             # Application entry point
└── README.md           # Project documentation
```

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory:
   ```bash
   cd Campus_Navigator
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The application will list all available locations on the campus.

3. Enter your **current location** when prompted.

4. Enter your **destination** when prompted.

5. The program will display the shortest path and the estimated travel time.

### Example

```text
Available locations:
- IT Lab
- Lecture Rooms
- Auditorium
- Library
- Cafe
...

Enter current location: IT Lab
Enter destination: Cafe

Shortest path:
IT Lab -> Lecture Rooms -> Auditorium -> Library -> Cafe
Estimated time: 7 minutes
```

## Data Format

The campus map is stored in `data/campus_map.json`. You can modify this file to add new locations or change connections. The format is an adjacency list where keys are locations and values are dictionaries of connected locations and their travel costs (weights).

```json
{
  "Location A": {
    "Location B": 5,
    "Location C": 10
  },
  "Location B": {
    "Location A": 5
  }
}
```

## Algorithms Used

- **Graph Representation**: Adjacency List
- **Pathfinding**: Dijkstra's Algorithm
