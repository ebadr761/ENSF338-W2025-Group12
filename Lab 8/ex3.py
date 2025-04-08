########################################################
# ex3.py
# Exercise 3: Kruskal MST using UNION-FIND.
########################################################

from ex1 import Graph, GraphNode

class UnionFind:
    """
    Disjoint-set (Union-Find) data structure for cycle detection,
    used in Kruskal's MST.
    """
    def __init__(self):
        # parent dict: maps a node to its parent
        self.parent = {}
        # rank dict: optional, used for union by rank
        self.rank = {}

    def make_set(self, node):
        # Each node is initially its own parent (self root)
        self.parent[node] = node
        self.rank[node] = 0

    def find(self, node):
        # Path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Union by rank
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False


class MSTGraph(Graph):
    """
    Extends the Graph from ex1 with an mst() method that uses Kruskal's algorithm.
    """
    def mst(self):
        """
        Returns a new MSTGraph object describing the MST of this graph,
        using Kruskal + Union-Find.
        If the graph is not connected, the MST will cover only the connected component(s).
        """
        # 1. Create new empty MSTGraph
        mst_graph = MSTGraph()

        # 2. Make a list of all edges in the current graph
        edges = []  # list of (w, node1, node2)
        for node, neighbors in self.adj_list.items():
            for nbr, w in neighbors.items():
                # To avoid duplicates in undirected graph, only consider (node < nbr) or something
                if node.data < nbr.data:
                    edges.append((w, node, nbr))

        # 3. Sort edges by weight
        edges.sort(key=lambda x: x[0])

        # 4. Initialize Union-Find
        uf = UnionFind()
        # make_set for all nodes
        for node in self.adj_list:
            uf.make_set(node)

        # 5. Kruskal’s
        for (w, n1, n2) in edges:
            if uf.union(n1, n2):
                # That means no cycle was formed, so add the edge to MST
                # Make sure we have the nodes in MST
                mst_n1 = mst_graph._findOrCreateNode(n1.data)
                mst_n2 = mst_graph._findOrCreateNode(n2.data)
                mst_graph.addEdge(mst_n1, mst_n2, w)

        return mst_graph

    # We reuse the _findOrCreateNode(...) logic from the ex1.Graph or copy it here:
    def _findOrCreateNode(self, data):
        for node in self.adj_list:
            if node.data == data:
                return node
        # If not found, add a new node
        return self.addNode(data)


def main():
    # Quick demonstration
    g = MSTGraph()
    g.importFromFile("random.dot")  # or some sample .dot file

    # Build MST
    mst_g = g.mst()

    print("Original Graph:")
    print(g)
    print("\nMST:")
    print(mst_g)

if __name__ == "__main__":
    main()
