########################################################
# ex1.py
# Exercise 1: A Graph class using adjacency lists.
########################################################

class GraphNode:
    """
    Simple wrapper to store node data, so that we can expand
    if needed. Alternatively, we can just store strings directly.
    """
    def __init__(self, data):
        self.data = data  # typically a string
        # You could add other fields if desired.

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"GraphNode({self.data})"


class Graph:
    def __init__(self):
        """
        Adjacency list stored as:
        self.adj_list = {
           nodeObject: { neighborNodeObject: weight, ... },
           ...
        }
        """
        self.adj_list = {}

    def addNode(self, data):
        """
        Creates a new graph node storing the string 'data',
        and adds it to the adjacency list (initially with no edges).
        Returns the newly created GraphNode object.
        """
        new_node = GraphNode(data)
        if new_node not in self.adj_list:
            self.adj_list[new_node] = {}
        return new_node

    def removeNode(self, node):
        """
        Removes 'node' and all its incident edges from the graph.
        """
        if node not in self.adj_list:
            return
        # Remove this node from other adjacency lists
        for neighbor in self.adj_list[node].keys():
            if neighbor in self.adj_list:
                self.adj_list[neighbor].pop(node, None)
        # Now remove it entirely
        self.adj_list.pop(node, None)

    def addEdge(self, n1, n2, weight=1):
        """
        Creates an undirected edge between n1 and n2 with the given weight.
        n1 and n2 must be GraphNode objects already in the graph.
        """
        if n1 not in self.adj_list:
            self.adj_list[n1] = {}
        if n2 not in self.adj_list:
            self.adj_list[n2] = {}
        self.adj_list[n1][n2] = weight
        self.adj_list[n2][n1] = weight

    def removeEdge(self, n1, n2):
        """
        Removes the edge between n1 and n2 (if it exists).
        """
        if n1 in self.adj_list:
            self.adj_list[n1].pop(n2, None)
        if n2 in self.adj_list:
            self.adj_list[n2].pop(n1, None)

    def importFromFile(self, filename):
        """
        Imports a graph description from a GraphViz file.
        The file is assumed to describe an undirected graph
        in the form:
          strict graph G {
             node1 -- node2 [weight=5];
             node3 -- node4;
             ...
          }

        If the file is invalid (e.g. not 'strict graph G'), return None.

        On success, returns self (the newly loaded graph).
        """
        try:
            with open(filename, 'r') as f:
                lines = [line.strip() for line in f.readlines()]

            # Basic checks
            if not lines:
                return None
            if not lines[0].startswith("strict graph G"):
                return None

            # Find the line with the opening brace { and the closing brace } 
            # (often lines[0] might be "strict graph G {", so let's handle that carefully)
            if "{" not in lines[0]:
                # if it's not on the same line, the next line should have it
                i = 1
                found_brace = False
                while i < len(lines):
                    if "{" in lines[i]:
                        found_brace = True
                        break
                    i += 1
                if not found_brace:
                    return None
                # Now i points to line with '{'
                start_index = i + 1
            else:
                # The '{' is on the first line after "strict graph G ..."
                start_index = 1

            # Similarly for the '}' we search from the bottom up
            end_index = len(lines) - 1
            found_close_brace = False
            while end_index >= 0:
                if "}" in lines[end_index]:
                    found_close_brace = True
                    break
                end_index -= 1
            if not found_close_brace:
                return None

            # Clear current graph
            self.adj_list.clear()

            # Parse edges between start_index and end_index
            for idx in range(start_index, end_index):
                line = lines[idx]
                if not line or line.startswith("}"):
                    break
                if line.startswith("//"):
                    # skip comment lines (just in case)
                    continue

                # Typical line example: node1 -- node2 [weight=10];
                # Remove trailing semicolon if present
                if line.endswith(";"):
                    line = line[:-1].strip()

                # If there's a '[weight=x]', let's isolate that
                weight = 1  # default
                left_bracket_idx = line.find("[")
                if left_bracket_idx != -1:
                    # parse out the weight
                    right_bracket_idx = line.find("]", left_bracket_idx)
                    if right_bracket_idx == -1:
                        # bracket not closed properly
                        return None
                    # substring of the form weight=...
                    bracket_content = line[left_bracket_idx+1:right_bracket_idx].strip()
                    # e.g. bracket_content = 'weight=45'
                    if bracket_content.startswith("weight="):
                        w_str = bracket_content[len("weight="):]
                        try:
                            weight = int(w_str)
                        except:
                            return None
                    # remove that bracketed text from the line
                    line = (line[:left_bracket_idx] + line[right_bracket_idx+1:]).strip()

                # Now line might look like "node1 -- node2"
                parts = line.split("--")
                if len(parts) != 2:
                    # not a valid edge definition
                    return None

                node1_str = parts[0].strip()
                node2_str = parts[1].strip()

                # Create/fetch the corresponding GraphNode objects
                node1_obj = self._findOrCreateNode(node1_str)
                node2_obj = self._findOrCreateNode(node2_str)

                # Add the edge
                self.addEdge(node1_obj, node2_obj, weight)

            return self

        except:
            return None

    def _findOrCreateNode(self, data):
        """
        Helper to find an existing node with the given data or create it.
        """
        # Because we're using GraphNode objects in a dictionary,
        # we need to see if a node with 'data' already exists.
        # We'll do a quick search.  Alternatively, we could keep a
        # dictionary from data->nodeObject, but let's do a small search here.
        for node in self.adj_list:
            if node.data == data:
                return node
        # If not found, add a new node
        return self.addNode(data)

    def __str__(self):
        """
        Return a brief string representation.
        """
        result = []
        for node, neighbors in self.adj_list.items():
            for nbr, w in neighbors.items():
                if str(node) < str(nbr):
                    result.append(f"{node.data} -- {nbr.data} (w={w})")
        return "\n".join(result)


# If you want to do quick tests:
if __name__ == "__main__":
    g = Graph()
    g.addNode("A")
    g.addNode("B")
    nC = g.addNode("C")
    g.addEdge(nC, g.addNode("D"), 10)
    print(g)
    # Try importing a small .dot file if desired
    # g.importFromFile("some_graph.dot")
    # print(g)
