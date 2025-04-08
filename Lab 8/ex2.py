########################################################
# ex2.py
# Exercise 2: Two Dijkstra's implementations (slow & fast),
# and performance measurement on random.dot.
########################################################

import time
import heapq
import statistics
import matplotlib.pyplot as plt  # For histogram

# If ex1.py is in the same folder:
from ex1 import Graph, GraphNode

class DijkstraGraph(Graph):
    """
    Inherits from Graph (adjacency list).
    Adds methods for slowSP and fastSP.
    """

    def slowSP(self, start_node):
        """
        Dijkstra's algorithm with O(V^2) selection:
        - distances dict
        - 'visited' set or logic
        - pick next node with smallest dist by linear search
        """
        dist = {}
        prev = {}
        for node in self.adj_list:
            dist[node] = float('inf')
            prev[node] = None
        dist[start_node] = 0

        unvisited = set(self.adj_list.keys())

        while unvisited:
            # 1. Pick node with smallest dist among unvisited (linear search)
            current = None
            current_dist = float('inf')
            for node in unvisited:
                if dist[node] < current_dist:
                    current_dist = dist[node]
                    current = node
            if current is None:
                break  # all unreachable

            unvisited.remove(current)

            # 2. Relax edges
            for neighbor, w in self.adj_list[current].items():
                if neighbor in unvisited:
                    alt = dist[current] + w
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        prev[neighbor] = current

        return dist, prev

    def fastSP(self, start_node):
        """
        Dijkstra's algorithm with a priority queue (heapq).
        - distances dict
        - uses a min-heap
        """
        dist = {}
        prev = {}
        for node in self.adj_list:
            dist[node] = float('inf')
            prev[node] = None

        dist[start_node] = 0

        # Min-heap of (distance, node)
        pq = [(0, start_node)]
        visited = set()

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            # Relax edges
            for neighbor, w in self.adj_list[current_node].items():
                alt = current_dist + w
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current_node
                    heapq.heappush(pq, (alt, neighbor))

        return dist, prev


def main():
    # 1. Load the graph from random.dot
    g = DijkstraGraph()
    g.importFromFile("random.dot")  # Adjust path as needed

    # 2. Gather times for all nodes for slowSP and fastSP
    all_nodes = list(g.adj_list.keys())

    slow_times = []
    fast_times = []

    # For each node as the source
    for source in all_nodes:
        # slow
        t0 = time.time()
        g.slowSP(source)
        t1 = time.time()
        slow_times.append(t1 - t0)

        # fast
        t2 = time.time()
        g.fastSP(source)
        t3 = time.time()
        fast_times.append(t3 - t2)

    # Compute average, max, min
    slow_avg = statistics.mean(slow_times)
    slow_max = max(slow_times)
    slow_min = min(slow_times)

    fast_avg = statistics.mean(fast_times)
    fast_max = max(fast_times)
    fast_min = min(fast_times)

    print("SLOW Dijkstra: avg=%.6f s, max=%.6f s, min=%.6f s" %
          (slow_avg, slow_max, slow_min))
    print("FAST Dijkstra: avg=%.6f s, max=%.6f s, min=%.6f s" %
          (fast_avg, fast_max, fast_min))

    # 3. Plot histogram
    plt.hist(slow_times, bins=30)  # One histogram for slow times
    plt.title("SlowSP Execution Times")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.show()

    plt.hist(fast_times, bins=30)  # Another histogram for fast times
    plt.title("FastSP Execution Times")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.show()

    # Add code or comments discussing results in your submission...


if __name__ == "__main__":
    main()
