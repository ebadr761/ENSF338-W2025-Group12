########################################################
# ex4.py
# Exercise 4: Adjacency matrix (Graph2) & DFS in both
########################################################

import time
import statistics

from ex1 import Graph, GraphNode

class Graph2:
    """
    Graph2 uses an adjacency matrix.

    We'll store:
    - self.nodes: a list of GraphNode objects
    - self.index_map: dict from GraphNode->int (for quick index lookup)
    - self.matrix: 2D list, matrix[i][j] = weight or 0 if no edge
    """
    def __init__(self):
        self.nodes = []
        self.index_map = {}
        self.matrix = []

    def addNode(self, data):
        """ Add a new node to our node list and expand the matrix. """
        new_node = GraphNode(data)
        if new_node in self.index_map:
            # Already exists
            return new_node
        self.nodes.append(new_node)
        index = len(self.nodes) - 1
        self.index_map[new_node] = index

        # Expand matrix with a new row+column
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0]*len(self.nodes))
        return new_node

    def removeNode(self, node):
        """ For simplicity, we won't fully implement remove in this example.
            One could shift matrix rows/cols, etc.
        """
        pass

    def addEdge(self, n1, n2, weight=1):
        if n1 not in self.index_map:
            self.addNode(n1.data)
        if n2 not in self.index_map:
            self.addNode(n2.data)
        i = self.index_map[n1]
        j = self.index_map[n2]
        self.matrix[i][j] = weight
        self.matrix[j][i] = weight  # undirected

    def removeEdge(self, n1, n2):
        i = self.index_map.get(n1, None)
        j = self.index_map.get(n2, None)
        if i is not None and j is not None:
            self.matrix[i][j] = 0
            self.matrix[j][i] = 0

    def dfs(self):
        """ Return a list of nodes in DFS order. We'll do a DFS from the first node, 
            then continue to unvisited nodes if the graph is not fully connected.
        """
        visited = set()
        result = []

        def dfs_visit(idx):
            visited.add(idx)
            result.append(self.nodes[idx])
            for nbr_idx in range(len(self.nodes)):
                if self.matrix[idx][nbr_idx] != 0 and nbr_idx not in visited:
                    dfs_visit(nbr_idx)

        # In case the graph is disconnected, run DFS from each unvisited node
        for start_idx in range(len(self.nodes)):
            if start_idx not in visited:
                dfs_visit(start_idx)

        return result

    def importFromFile(self, filename):
        """ 
        Re-builds the adjacency matrix from a .dot file (undirected).
        Similar logic to ex1, but we store in matrix form.
        """
        # Clear
        self.nodes = []
        self.index_map = {}
        self.matrix = []

        # A quick approach: parse edges, then call addEdge
        # A direct or simpler parse can be used, basically the same
        # pattern as in ex1.
        # For brevity, re-implement a minimal version here:
        try:
            with open(filename, 'r') as f:
                lines = [line.strip() for line in f.readlines()]
            if not lines:
                return None
            if not lines[0].startswith("strict graph G"):
                return None

            # find { and }
            # (similar to ex1)
            start_index = 1
            end_index = len(lines) - 1
            # search ...
            while start_index < len(lines) and "{" not in lines[start_index]:
                start_index += 1
            while end_index >= 0 and "}" not in lines[end_index]:
                end_index -= 1
            if start_index >= len(lines) or end_index < 0:
                return None

            for idx in range(start_index+1, end_index):
                line = lines[idx]
                if not line or line.startswith("}"):
                    break
                if line.endswith(";"):
                    line = line[:-1].strip()
                weight = 1
                lb = line.find("[")
                if lb != -1:
                    rb = line.find("]", lb)
                    if rb == -1:
                        return None
                    bracket_content = line[lb+1:rb].strip()
                    if bracket_content.startswith("weight="):
                        w_str = bracket_content[len("weight="):]
                        weight = int(w_str)
                    line = (line[:lb] + line[rb+1:]).strip()
                parts = line.split("--")
                if len(parts) != 2:
                    return None
                n1_str = parts[0].strip()
                n2_str = parts[1].strip()

                n1_obj = self._findOrCreateNode(n1_str)
                n2_obj = self._findOrCreateNode(n2_str)
                self.addEdge(n1_obj, n2_obj, weight)
            return self
        except:
            return None

    def _findOrCreateNode(self, data):
        # see if we already have a node with that data
        for n in self.index_map:
            if n.data == data:
                return n
        return self.addNode(data)


# Extend the original Graph class (adjacency list) with DFS
def dfs_list(graph):
    """
    Returns a list of nodes in DFS order for the adjacency-list-based Graph.
    We'll do a standard adjacency-list DFS from the first node, 
    continuing if disconnected.
    """
    visited = set()
    result = []

    def dfs_visit(node):
        visited.add(node)
        result.append(node)
        for nbr in graph.adj_list[node].keys():
            if nbr not in visited:
                dfs_visit(nbr)

    # Possibly disconnected, so start DFS from each node
    for node in graph.adj_list.keys():
        if node not in visited:
            dfs_visit(node)
    return result


def main():
    # 1. Build adjacency-list Graph and adjacency-matrix Graph2 from the same .dot
    from ex1 import Graph
    g_list = Graph()
    g_list.importFromFile("random.dot")

    g_matrix = Graph2()
    g_matrix.importFromFile("random.dot")

    # 2. Repeatedly time DFS
    times_list = []
    times_matrix = []
    import time

    for _ in range(10):
        t0 = time.time()
        dfs_list(g_list)
        t1 = time.time()
        times_list.append(t1 - t0)

        t2 = time.time()
        g_matrix.dfs()
        t3 = time.time()
        times_matrix.append(t3 - t2)

    # 3. Print results
    avg_list = statistics.mean(times_list)
    max_list = max(times_list)
    min_list = min(times_list)

    avg_matrix = statistics.mean(times_matrix)
    max_matrix = max(times_matrix)
    min_matrix = min(times_matrix)

    print("Adj-list DFS: avg=%.6f, max=%.6f, min=%.6f" % (avg_list, max_list, min_list))
    print("Adj-mat DFS: avg=%.6f, max=%.6f, min=%.6f" % (avg_matrix, max_matrix, min_matrix))

    # 4. In your final submission, add comments about why adjacency-list DFS 
    #    is typically more efficient on sparse graphs than adjacency-matrix.


if __name__ == "__main__":
    main()
