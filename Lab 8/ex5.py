########################################################
# ex5.py
# Exercise 5: DAG check and Topological Sort
########################################################

"""
Q1: Which algorithm for topological sorting?
A: We can use a DFS-based approach (sometimes called the depth-first search
   topological sort) or Kahn's algorithm (BFS-based). 
   We'll demonstrate the DFS-based approach. 
   We choose it because it is straightforward to implement recursively:
   - run DFS
   - after visiting all descendants of a node, push the node onto a stack
   - then reverse the stack at the end for the topological order
"""

from ex1 import Graph, GraphNode

class DAGGraph(Graph):
    """
    We'll treat edges as if they are directed in adjacency.
    That means if you do addEdge(n1, n2), we interpret it as n1 -> n2 only.

    For a truly undirected structure, topological sort doesn't make sense
    unless it's a tree or has no cycles, so let's override addEdge here
    to store direction.
    """
    def addEdge(self, n1, n2, weight=1):
        # Instead of storing both ways, just store n1->n2
        if n1 not in self.adj_list:
            self.adj_list[n1] = {}
        if n2 not in self.adj_list:
            self.adj_list[n2] = {}
        self.adj_list[n1][n2] = weight
        # not adding the reverse direction, i.e. no self.adj_list[n2][n1]

    def isdag(self):
        """
        Returns True if the graph has no cycles, False otherwise.
        We'll do a DFS-based cycle detection for directed graphs.
        We have 3 states: unvisited, visiting, visited:
          unvisited (0)
          visiting (1)
          visited (2)
        If we ever go from a 'visiting' node to another 'visiting' node, 
        there's a cycle.
        """
        state = {}  # node -> 0/1/2

        for node in self.adj_list:
            state[node] = 0  # unvisited

        def dfs_cycle(node):
            if state[node] == 1:
                # found a node we are currently visiting -> cycle
                return True
            if state[node] == 2:
                # already fully visited -> no cycle from here
                return False
            # mark as visiting
            state[node] = 1
            # explore
            for nbr in self.adj_list[node]:
                if dfs_cycle(nbr):
                    return True
            # mark as visited
            state[node] = 2
            return False

        for node in self.adj_list:
            if state[node] == 0:
                if dfs_cycle(node):
                    return False
        return True

    def toposort(self):
        """
        Returns a list of nodes in topological order if DAG, 
        or None if there's a cycle.
        """
        if not self.isdag():
            return None

        visited = set()
        result_stack = []

        def dfs_topo(node):
            visited.add(node)
            for nbr in self.adj_list[node]:
                if nbr not in visited:
                    dfs_topo(nbr)
            # Once done with children, push node onto stack
            result_stack.append(node)

        for node in self.adj_list:
            if node not in visited:
                dfs_topo(node)

        # The result_stack will have the reverse of topological order, so reverse it
        result_stack.reverse()
        return result_stack


def main():
    g = DAGGraph()

    # Suppose we manually add some edges that represent a DAG:
    nA = g.addNode("A")
    nB = g.addNode("B")
    nC = g.addNode("C")
    nD = g.addNode("D")

    g.addEdge(nA, nB)  # A->B
    g.addEdge(nA, nC)  # A->C
    g.addEdge(nB, nD)  # B->D
    g.addEdge(nC, nD)  # C->D

    # Now let's check
    print("Is DAG?", g.isdag())
    topo_order = g.toposort()
    print("Topological order:", [str(n) for n in topo_order])

    # If we add a cycle:
    g.addEdge(nD, nA)  # D->A introduces cycle
    print("Is DAG after adding D->A?", g.isdag())
    print("Topological order now is:", g.toposort())  # should be None


if __name__ == "__main__":
    main()
