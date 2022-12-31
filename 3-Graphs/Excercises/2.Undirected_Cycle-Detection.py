class Graph:
    def __init__(self, num_nodes):
        self.adj_list = {i: [] for i in range(num_nodes)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

def find_cycle(G):
    # Initialize the stack and visited dictionary
    S = []
    visited = {}

    # For each unvisited node in the graph
    for u in G.adj_list.keys():
        if not visited.get(u):
            # Add u to the stack and mark it as visited
            S.append(u)
            visited[u] = True
            # For each edge (u, v) incident to u
            for v in G.adj_list[u]:
                # If v is not marked as visited
                if not visited.get(v):
                    # Recursively invoke the DFS function on v
                    result = DFS(v, S, visited, G)
                    # If a cycle was found, return it
                    if result is not None:
                        return result
                # Otherwise, if v is in the stack S
                elif v in S:
                    # Return v as the first node in the cycle
                    return v
    # Return "no cycle found"
    return "no cycle found"

def DFS(u, S, visited, G):
    # Add u to the stack and mark it as visited
    S.append(u)
    visited[u] = True
    # For each edge (u, v) incident to u
    for v in G.adj_list[u]:
        # If v is not marked as visited
        if not visited.get(v):
            # Recursively invoke the DFS function on v
            result = DFS(v, S, visited, G)
            # If a cycle was found, return it
            if result is not None:
                return result
        # Otherwise, if v is in the stack S
        elif v in S:
            # Return v as the first node in the cycle
            return v
    # Remove u from the stack
    S.pop()
    return None

# Create a graph with 5 nodes and 6 edges
G = Graph(5)
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 0)
G.add_edge(4, 1)

# Find a cycle in the graph
result = find_cycle(G)
print(result)  # Output
