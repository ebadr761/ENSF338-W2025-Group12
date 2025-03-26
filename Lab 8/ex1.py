class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def addNode(self, data):
        if data not in self.adj_list:
            self.adj_list[data] = []
            return GraphNode(data)
    
    def removeNode(self, node):
        if node in self.adj_list:
            del self.adj_list[node]
            for neighbors in self.adj_list.values():
                neighbors[:] = [n for n in neighbors if n[0] != node]
    
    def addEdge(self, n1, n2, weight=1):
        if n1 in self.adj_list and n2 in self.adj_list:
            self.adj_list[n1].append((n2, weight))
            self.adj_list[n2].append((n1, weight))
    
    def removeEdge(self, n1, n2):
        if n1 in self.adj_list and n2 in self.adj_list:
            self.adj_list[n1] = [(node, w) for node, w in self.adj_list[n1] if node != n2]
            self.adj_list[n2] = [(node, w) for node, w in self.adj_list[n2] if node != n1]
    
    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
            
            if not lines[0].startswith("strict graph"):
                return None
            
            self.adj_list.clear()
            
            for line in lines[1:]:
                line = line.strip().rstrip(';')
                if not line:
                    continue
                
                parts = line.split('--')
                if len(parts) != 2:
                    return None
                
                node1, rest = parts[0].strip(), parts[1].strip()
                weight = 1
                
                if '[' in rest:
                    node2, attr = rest.split('[')
                    node2 = node2.strip()
                    attr = attr.strip(']')
                    
                    if 'weight=' in attr:
                        weight = int(attr.split('=')[1])
                else:
                    node2 = rest.strip()
                
                self.addNode(node1)
                self.addNode(node2)
                self.addEdge(node1, node2, weight)
            
            return self
        except:
            return None
