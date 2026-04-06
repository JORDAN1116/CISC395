import heapq

def prim(graph: dict):
    total_weight = 0
    mst = []
    pq = []
    vertices = list(graph.keys())
    start_vertex = vertices[0]
    unvisited = set(vertices)

    # Push dummy edge to start the loop
    heapq.heappush(pq, (0, (start_vertex, start_vertex)))

    while pq:  # while pq is not empty
        w, (u, v) = heapq.heappop(pq)  # remove the cheapest edge
        if v in unvisited:  # if v is in unvisited
            unvisited.remove(v)  # remove it from unvisited
            if u != v: # skip dummy loop, do not add the dummy self edge to mst
                mst.append((u, v, w))  # add this edge to mst
                total_weight += w  # update total weight

        for neighbor in graph[v]:  # for each v's neighbor
            if neighbor in unvisited:  # if v is in unvisited
                heapq.heappush(pq, (graph[v][neighbor], (v, neighbor)))  # add it to pq

    return mst, total_weight


def kruskal(graph:dict):
    total_weight = 0
    mst = list()
    edges = list()
    added = set()
    for v in graph:
        for u, w in graph[v].items():
            if (u, v) not in added:  # avoid add duplicates edges if u -> v is in added, do not add v-> u
                edges.append((v, u, w))
                added.add((v, u))

    # sort all edges based on the weight at index 2 in (u, v, w)
    sorted_edges = sorted(edges, key=lambda edge:edge[2])
    #print(sorted_edges)
    union_find = UnionFind(graph.keys())
    #print(union_find)
    for edge in sorted_edges:
        #edge = sorted_edges.pop(0)
        #u = edge[0]
        #v = edge[1]
        u, v, w = edge
        if not union_find.is_connected(u, v): # if u and v are not connected
            mst.append(edge) # add edge to mst
            total_weight += w
            union_find.union(u, v) # connect u and v
        #print(union_find)
    return mst, total_weight

def boruvka(graph: dict):
    uf = UnionFind(graph.keys())
    mst = []
    total_weight = 0

    # Convert adjacency dict to edge list (avoid duplicates)
    edges = []
    added = set()
    for v in graph:
        for u, w in graph[v].items():
            if (u, v) not in added:
                edges.append((v, u, w))
                added.add((v, u))

    num_components = uf.num_of_components() # num of components is the number of vertices
    # Continue until only one component remains
    while num_components > 1:
        min_edges = dict()
        # Step 1: find min_edges edge for each component
        for u, v, w in edges:
            u_id = uf.find(u) # component number of u
            v_id = uf.find(v) # component number of v
            #if u_id != v_id: #
            if not uf.is_connected(u, v):
                if u_id not in min_edges or w < min_edges[u_id][2]:
                    min_edges[u_id] = (u, v, w)
                if v_id not in min_edges or w < min_edges[v_id][2]:
                    min_edges[v_id] = (u, v, w)
        print('min_edges:', min_edges)
        # Step 2: add all unique min_edges edges
        for edge in min_edges.values():
            u, v, w = edge
            if not uf.is_connected(u, v):
                uf.union(u, v)  # if u and v are not connected
                mst.append(edge) # add this edge to mst
                total_weight += w

        num_components = uf.num_of_components() # update based on num of components

    return mst, total_weight

class UnionFind:
    def __init__(self, vertices):
        # n is the number of nodes
        self.ids = dict(zip(vertices, range(len(vertices))))

    def find(self, p):
        return self.ids[p]

    def is_connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        value = self.ids[p]
        for i in self.ids.keys():
            if self.ids[i] == value:
                self.ids[i] = self.ids[q]

    def num_of_components(self):
        return len(set(self.ids.values()))

    def get_components(self):
        components = dict()
        for k, v in self.ids.items():
            components[v] = components.get(v, []) + [k]
        return components

    def __str__(self):
        return str(self.ids)



if __name__ == "__main__":
    """
    graph = [
    ("JFK", "PVD", 144),
    ("JFK", "BOS", 187),
    ("JFK", "ORD", 740),
    ("JFK", "DFW", 1391),
    ("JFK", "BWI", 184),
    ("JFK", "MIA", 1090),
    ("PVD", "ORD", 849),
    ("ORD", "BOS", 867),
    ("ORD", "SFO", 1846),
    ("ORD", "DFW", 802),
    ("ORD", "BWI", 621),
    ("BWI", "MIA", 946),
    ("BOS", "SFO", 2704),
    ("BOS", "MIA", 1258),
    ("SFO", "DFW", 1464),
    ("MIA", "DFW", 1121),
    ("MIA", "LAX", 2342),
    ("SFO", "LAX", 337),
    ("LAX", "DFW", 1235)
    ]
    graph = transform(graph)
    print(graph)"""
    graph = {'JFK': {'PVD': 144, 'BOS': 187, 'ORD': 740, 'DFW': 1391, 'BWI': 184, 'MIA': 1090},
         'PVD': {'JFK': 144, 'ORD': 849},
         'BOS': {'JFK': 187, 'ORD': 867, 'SFO': 2704, 'MIA': 1258},
         'ORD': {'JFK': 740, 'PVD': 849, 'BOS': 867, 'SFO': 1846, 'DFW': 802, 'BWI': 621},
         'DFW': {'JFK': 1391, 'ORD': 802, 'SFO': 1464, 'MIA': 1121, 'LAX': 1235},
         'BWI': {'JFK': 184, 'ORD': 621, 'MIA': 946},
         'MIA': {'JFK': 1090, 'BWI': 946, 'BOS': 1258, 'DFW': 1121, 'LAX': 2342},
         'SFO': {'ORD': 1846, 'BOS': 2704, 'DFW': 1464, 'LAX': 337},
         'LAX': {'MIA': 2342, 'SFO': 337, 'DFW': 1235}}
    #mst1 = MST.prim(graph)
    #print(mst1)

    graph2 = {
        'a': {'b':7, 'd':5},
        'b': {'a':7, 'c':8, 'd':9, 'e':7},
        'c': {'b':8, 'e':5},
        'd': {'a':5, 'b':9, 'e':15, 'f':6},
        'e': {'b':7, 'c':5, 'd':15, 'f':8, 'g':9},
        'f': {'d':6, 'e':8, 'g':11},
        'g': {'e':9, 'f':11}
    }
    #mst2 = MST.prim(graph2)
    #print(mst2)

    graph3 = {
        'a' : {'b':10, 'c':12},
        'b' : {'c':5, 'a':10},
        'c' : {'a':10}
    }
    #mst3 = MST.prim(graph3)
    #print(mst3)
    #graph = transform_back(graph)
    #sorted_edges = sorted(graph, key=lambda edge: edge[2])
    #v = "abcdefg"
    #u = UnionFind(v)
    #print(u)
    #u.union('c', 'd')
    #print(u)
    #u.union('a', 'c')
    #print(u)
    #x = u.is_connected('c', 'd')
    #y = u.is_connected('a', 'c')

    # # print('prim', prim(graph))
    # # print('kruskal', kruskal(graph))
    print('boruvka', boruvka(graph))
    # # print('prim', prim(graph2))
    # # print('kruskal', kruskal(graph2))
    print('boruvka', boruvka(graph2))
    # # print('prim', prim(graph3))
    # # print('kruskal', kruskal(graph3))
    print('boruvka', boruvka(graph3))