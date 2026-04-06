import heapq
# test case
# adjacency map

G = {
 'A': {'B': 7, 'D': 5},
 'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
 'C': {'B': 8, 'E': 5},
 'D': {'A': 5, 'B': 9, 'E': 12, 'F': 6},
 'E': {'B': 7, 'C': 5, 'D': 12, 'F': 8, 'G': 9},
 'F': {'D': 6, 'E': 8, 'G': 11},
 'G': {'E': 9, 'F': 11}
}

# weight of edge between D and F
#G['D']['F']
# neighbors of E
#G['E'].keys()

def dijkstra(graph, start):
    unvisited = set(graph.keys())
    q = list() # priority queue
    distance = dict() # store shortest distance from s to every another vertex
    for vertex in graph.keys():
        distance[vertex] = float('inf')
    distance[start] = 0
    # add first pair to pq (path_cost, vertex)
    heapq.heappush(q, (0, start))
    while q:
        d, u = heapq.heappop(q)
        if u in unvisited:
            unvisited.remove(u)
            for v in graph[u].keys():
                if v in unvisited:
                    temp = distance[u] + graph[u][v]
                    if temp < distance[v]:
                        # update
                        distance[v] = temp # better path found!
                        heapq.heappush(q, (temp, v))
    return distance


def bellman_ford(graph, start):
    distance = dict()
    for vertex in graph.keys():
        distance[vertex] = float('inf')
    distance[start] = 0
    # edge (u, v, w)
    edges = list()
    for u, vw in graph.items():
        for v, w in vw.items():
            edges.append((u, v, w))
    # repeat number of vertices - 1
    for i in range(len(graph.keys())-1):
        for u, v, w in edges:
            temp = distance[u] + w
            if temp < distance[v]:
                distance[v] = temp
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            print('negative cycle detected!')
            return None
    return distance

def floyd_warshall(graph):
    distance = {key: dict.fromkeys(graph.keys(), float('inf')) for key in graph.keys()}
    # update diagonal elements
    for vertex in graph.keys():
        distance[vertex][vertex] = 0
        for j, w in graph[vertex].items():
            distance[vertex][j] = w
    for k in graph.keys():
        for i in graph.keys():
            for j in graph.keys():
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

if __name__ == '__main__':
    print('dijkstra: ', dijkstra(G, 'A'))
    print('bellman ford: ', bellman_ford(G, 'A'))
    print('floyd warshall: ', floyd_warshall(G))





    
    
