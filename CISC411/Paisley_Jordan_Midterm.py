import heapq
from math import log2, ceil
from random import randint

# --- Tree Structures ---

class AVLTree:
    class Node:
        def __init__(self, element=None):
            self.element = element
            self.left = None
            self.right = None
            self.height = 1

        def get_children(self):
            if self.left is not None:
                yield self.left
            if self.right is not None:
                yield self.right

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.__insert_helper(key, self.root)

    def __insert_helper(self, key, node):
        if node is None:
            return AVLTree.Node(key)
        else:
            if key <= node.element:
                node.left = self.__insert_helper(key, node.left)
            elif key > node.element:
                node.right = self.__insert_helper(key, node.right)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance_factor = self.balance_factor(node)

        if balance_factor > 1:
            if self.balance_factor(node.left) >= 0:
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        if balance_factor < -1:
            if self.balance_factor(node.right) <= 0:
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        return node

    def left_rotate(self, z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        t2 = y.right
        y.right = z
        z.left = t2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def delete(self, key):
        if self.root is None:
            return None
        self.root = self.__delete_helper(key, self.root)

    def __delete_helper(self, key, node):
        if node is None:
            return None
        elif key < node.element:
            node.left = self.__delete_helper(key, node.left)
        elif key > node.element:
            node.right = self.__delete_helper(key, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                successor = self.get_successor(node.right)
                node.element = successor.element
                node.right = self.__delete_helper(successor.element, node.right)
        return node

    @staticmethod
    def get_successor(node):
        while node.left is not None:
            node = node.left
        return node

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    @staticmethod
    def get_height(node):
        if node is None:
            return 0
        return node.height

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        size = 2 * 2 ** int(ceil(log2(self.n))) - 1
        self.segment_tree = [0] * size
        self.__build_helper(0, self.n-1, 0)

    def __build_helper(self, start, end, i):
        if start == end:
            self.segment_tree[i] = self.arr[start]
            return self.segment_tree[i]
        mid = (start + end) // 2
        self.segment_tree[i] = self.__build_helper(start, mid, 2 * i + 1) + \
                               self.__build_helper(mid+1, end, 2 * i + 2)
        return self.segment_tree[i]

# --- Sorting Algorithms ---

def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        for j in range(n-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

def selection_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq

def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        marked = seq[i]
        j = i
        while j >= 1 and seq[j-1] > marked:
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = marked
    return seq

def shell_sort(seq):
    n = len(seq)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = seq[i]
            j = i
            while j >= interval and seq[j-interval] > temp:
                seq[j] = seq[j-interval]
                j -= interval
            seq[j] = temp
        interval //= 2
    return seq

def partition(seq, start, end):
    pivot = seq[end]
    left = start
    right = end - 1
    while left <= right:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and seq[right] >= pivot:
            right -= 1
        if left <= right:
            seq[left], seq[right] = seq[right], seq[left]
            left += 1
            right -= 1
    seq[left], seq[end] = seq[end], seq[left]
    return left

def quick_sort(seq, start, end):
    if start >= end:
        return seq
    p = partition(seq, start, end)
    quick_sort(seq, start, p-1)
    quick_sort(seq, p+1, end)
    return seq

def merge_sort(seq):
    n = len(seq)
    if n < 2:
        return seq
    s1 = seq[:n//2]
    s2 = seq[n//2:]
    merge_sort(s1)
    merge_sort(s2)
    return merge(seq, s1, s2)

def merge(s, s1, s2):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1
    return s

def heapify(seq, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and seq[i] < seq[l]:
        largest = l
    if r < n and seq[largest] < seq[r]:
        largest = r
    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        heapify(seq, n, largest)

def heap_sort(seq):
    n = len(seq)
    for i in range(n // 2 - 1, -1, -1):
        heapify(seq, n, i)
    for j in range(n-1, 0, -1):
        seq[j], seq[0] = seq[0], seq[j]
        heapify(seq, j, 0)
    return seq

# --- Graph Algorithms ---

class UnionFind:
    def __init__(self, vertices):
        self.ids = dict(zip(vertices, range(len(vertices))))

    def find(self, p):
        return self.ids[p]

    def is_connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        p_root = self.ids[p]
        q_root = self.ids[q]
        if p_root != q_root:
            for vertex in self.ids:
                if self.ids[vertex] == p_root:
                    self.ids[vertex] = q_root

    def num_of_components(self):
        return len(set(self.ids.values()))

    def get_components(self):
        components = {}
        for k, v in self.ids.items():
            components[v] = components.get(v, []) + [k]
        return components

def bfs(graph, start_v):
    visited = []
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            for neighbor in graph[v].keys():
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

def dfs(graph, start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for neighbor in graph[v].keys():
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
    return visited

def uniform_cost_search(graph, start_v):
    pq = []
    visited = []
    heapq.heappush(pq, (0, start_v))
    lookup_dict = {start_v: 0}
    while pq:
        cost, v = heapq.heappop(pq)
        if v not in visited:
            visited.append(v)
            for neighbor, weight in graph[v].items():
                new_weight = cost + weight
                if neighbor not in lookup_dict or new_weight < lookup_dict[neighbor]:
                    lookup_dict[neighbor] = new_weight
                    heapq.heappush(pq, (new_weight, neighbor))
    return visited

def prim(graph: dict):
    total_weight = 0
    mst = []
    pq = []
    vertices = list(graph.keys())
    if not vertices: return mst, 0
    start_vertex = vertices[0]
    unvisited = set(vertices)
    heapq.heappush(pq, (0, (start_vertex, start_vertex)))
    while pq:
        w, (u, v) = heapq.heappop(pq)
        if v in unvisited:
            unvisited.remove(v)
            if u != v:
                mst.append((u, v, w))
                total_weight += w
            for neighbor in graph[v]:
                if neighbor in unvisited:
                    heapq.heappush(pq, (graph[v][neighbor], (v, neighbor)))
    return mst, total_weight

def kruskal(graph: dict):
    total_weight = 0
    mst = []
    edges = []
    seen = set()
    for u in graph:
        for v, w in graph[u].items():
            if (v, u) not in seen:
                edges.append((u, v, w))
                seen.add((u, v))
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(graph.keys())
    for u, v, w in edges:
        if not uf.is_connected(u, v):
            mst.append((u, v, w))
            total_weight += w
            uf.union(u, v)
    return mst, total_weight

def boruvka(graph: dict):
    uf = UnionFind(graph.keys())
    mst = []
    total_weight = 0
    edges = []
    seen = set()
    for u in graph:
        for v, w in graph[u].items():
            if (v, u) not in seen:
                edges.append((u, v, w))
                seen.add((u, v))
    num_components = uf.num_of_components()
    while num_components > 1:
        min_edges = {}
        for u, v, w in edges:
            if not uf.is_connected(u, v):
                u_id = uf.find(u)
                v_id = uf.find(v)
                if u_id not in min_edges or w < min_edges[u_id][2]:
                    min_edges[u_id] = (u, v, w)
                if v_id not in min_edges or w < min_edges[v_id][2]:
                    min_edges[v_id] = (u, v, w)
        if not min_edges: break
        for u, v, w in min_edges.values():
            if not uf.is_connected(u, v):
                uf.union(u, v)
                mst.append((u, v, w))
                total_weight += w
        num_components = uf.num_of_components()
    return mst, total_weight

def dijkstra(graph, start):
    unvisited = set(graph.keys())
    q = []
    distance = {v: float('inf') for v in graph}
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, u = heapq.heappop(q)
        if u in unvisited:
            unvisited.remove(u)
            for v, weight in graph[u].items():
                if v in unvisited:
                    temp = distance[u] + weight
                    if temp < distance[v]:
                        distance[v] = temp
                        heapq.heappush(q, (temp, v))
    return distance

def bellman_ford(graph, start):
    distance = {v: float('inf') for v in graph}
    distance[start] = 0
    edges = [(u, v, w) for u in graph for v, w in graph[u].items()]
    for _ in range(len(graph) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            return None
    return distance

def floyd_warshall(graph):
    distance = {u: {v: float('inf') for v in graph} for u in graph}
    for v in graph:
        distance[v][v] = 0
        for neighbor, weight in graph[v].items():
            distance[v][neighbor] = weight
    for k in graph:
        for i in graph:
            for j in graph:
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

def shortest_path(graph, start, goal):
    """
    Returns the shortest path from start to goal in a weighted graph with nonnegative edge weights.
    If no path exists, return an empty list.
    """
    if start not in graph or goal not in graph:
        return []
    
    unvisited = set(graph.keys())
    q = []
    distance = {v: float('inf') for v in graph}
    predecessor = {v: None for v in graph}
    
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        d, u = heapq.heappop(q)
        if u == goal:
            break
        if u in unvisited:
            unvisited.remove(u)
            for v, weight in graph[u].items():
                if v in unvisited:
                    temp = distance[u] + weight
                    if temp < distance[v]:
                        distance[v] = temp
                        predecessor[v] = u
                        heapq.heappush(q, (temp, v))
    
    path = []
    curr = goal
    while curr is not None:
        path.insert(0, curr)
        curr = predecessor[curr]
    
    if path and path[0] == start:
        return path
    else:
        return []

def is_tree(graph):
    """
    Returns True if an undirected graph is a tree, and False otherwise.
    A graph is a tree if it is connected and contains no cycle.
    """
    if not graph:
        return False
    
    # A connected graph with V vertices is a tree if and only if it has V-1 edges.
    v = len(graph)
    e = 0
    for neighbors in graph.values():
        e += len(neighbors)
    e //= 2 # Undirected graph, each edge is counted twice
    
    if e != v - 1:
        return False
    
    return count_components(graph) == 1

def prim_mst_cost(graph, start):
    """
    Uses Prim's algorithm to return the total cost of the MST.
    Returns None if the graph is not fully connected.
    """
    if not graph or start not in graph:
        return None
    
    total_cost = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        cost, u = heapq.heappop(pq)
        if u not in visited:
            visited.add(u)
            total_cost += cost
            for v, weight in graph[u].items():
                if v not in visited:
                    heapq.heappush(pq, (weight, v))
    
    if len(visited) == len(graph):
        return total_cost
    else:
        return None

# --- Midterm Task: count_components using BFS ---

def count_components(graph):
    """
    Returns the number of connected components in an undirected graph using BFS.
    """
    visited = set()
    count = 0
    for vertex in graph:
        if vertex not in visited:
            # Found a new component, start BFS
            queue = [vertex]
            visited.add(vertex)
            while queue:
                u = queue.pop(0)
                for v in graph[u].keys():
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            count += 1
    return count

if __name__ == "__main__":
    # Test cases for count_components
    g1 = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1},
        'D': {'E': 1},
        'E': {'D': 1},
        'F': {}
    }
    print(f"Graph 1 components: {count_components(g1)}") # Expected: 3

    g2 = {
        'A': {'B': 7, 'D': 5},
        'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
        'C': {'B': 8, 'E': 5},
        'D': {'A': 5, 'B': 9, 'E': 12, 'F': 6},
        'E': {'B': 7, 'C': 5, 'D': 12, 'F': 8, 'G': 9},
        'F': {'D': 6, 'E': 8, 'G': 11},
        'G': {'E': 9, 'F': 11}
    }
    print(f"Graph 2 components: {count_components(g2)}") # Expected: 1

    # Test case for shortest_path
    print(f"Shortest path from A to G in Graph 2: {shortest_path(g2, 'A', 'G')}") # Expected: ['A', 'D', 'F', 'G']

    # Test cases for is_tree
    t1 = {'A': {'B': 1}, 'B': {'A': 1, 'C': 1}, 'C': {'B': 1}}
    # V=3, E=2. Connected. Tree.
    print(f"Is t1 a tree? {is_tree(t1)}") # Expected: True
    t2 = {'A': {'B': 1, 'C': 1}, 'B': {'A': 1, 'C': 1}, 'C': {'B': 1, 'A': 1}}
    # V=3, E=3. Cycle. Not a tree.
    print(f"Is t2 a tree? {is_tree(t2)}") # Expected: False (cycle)
    t3 = {'A': {'B': 1}, 'B': {'A': 1}, 'C': {'D': 1}, 'D': {'C': 1}}
    # V=4, E=2. Disconnected. Not a tree.
    print(f"Is t3 a tree? {is_tree(t3)}") # Expected: False (disconnected)

    # Test cases for prim_mst_cost
    g_mst = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1},
        'C': {'A': 3, 'B': 1, 'D': 4},
        'D': {'B': 1, 'C': 4}
    }
    # MST: A-B (2), B-C (1), B-D (1). Total: 4
    print(f"Prim MST cost for g_mst: {prim_mst_cost(g_mst, 'A')}") # Expected: 4
    print(f"Prim MST cost for Graph 1 (disconnected): {prim_mst_cost(g1, 'A')}") # Expected: None
