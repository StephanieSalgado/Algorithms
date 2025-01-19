"""
Stephanie Salgado

April 29 2024

This code finds the shortest paths from a user-specified source node to all 
other nodes in a weighted graph using Dijkstra's algorithm. It then displays 
both the shortest distances and the corresponding paths.
"""
def dijkstra(graph, start):
    # Initialize the current distance dictionary with infinite distances
    curr_dist = {node: float('infinity') for node in graph}
    curr_dist[start] = 0

    # Initialize the predecessor dictionary
    pred = {node: None for node in graph}

    # Initialize the to-be-checked list with all nodes
    to_be_checked = list(graph.keys())

    # While there are nodes left to be checked
    while to_be_checked:
        # Find the node with the minimum current distance
        min_node = min(to_be_checked, key=lambda x: curr_dist[x])

        # Remove the node from the to-be-checked list
        to_be_checked.remove(min_node)

        # For each neighbor of the current node
        for neighbor in graph[min_node]:
            # Calculate the new distance to the neighbor
            new_dist = curr_dist[min_node] + graph[min_node][neighbor]

            # If the new distance is smaller than the current distance
            if new_dist < curr_dist[neighbor]:
                # Update the current distance and set the predecessor
                curr_dist[neighbor] = new_dist
                pred[neighbor] = min_node

    return curr_dist, pred

# Define the graph as an adjacency matrix
graph = {
    'a': {'b': 2, 'h': 10},
    'b': {'a': 2, 'c': 3, 'd': 4},
    'c': {'b': 3},
    'd': {'b': 4, 'e': 5},
    'e': {'d': 5, 'f': 3},
    'f': {'e': 3, 'g': 7},
    'g': {'f': 7, 'h': 1},
    'h': {'a': 10, 'g': 1}
}

# Get user input for the source node
source = input("Enter the source node: ")

# Find the shortest path from the source node to all other nodes in the graph
distances, pred = dijkstra(graph, source)

# Display the shortest distance from the source node to all other nodes in the graph
print("\nShortest distances from node", source + ":")
for node, dist in distances.items():
    print(f"To node {node}: {'Infinity' if dist == float('inf') else dist}")

# Display the path with the shortest distance from the source node to all other nodes in the graph
print("\nShortest paths from node", source + ":")
for node, dist in distances.items():
    if dist != float('infinity'):
        path = []
        dest = node
        while dest:
            path.append(dest)
            dest = pred.get(dest)
        path = path[::-1]
        print(f"To node {node}: {' -> '.join(path)}, Distance: {dist}")
