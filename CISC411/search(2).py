"""
adjacency map
"""
import heapq

graph = {
    'A': {'B':7, 'D':5},
    'B': {'A':7, 'D':9, 'C':8, 'E':7},
    'C': {'B':8, 'E':5},
    'D': {'A':5, 'B':9, 'E':12, 'F':6},
    'E': {'B':7, 'C':5, 'D':12, 'F':8, 'G':9},
    'F': {'D':6, 'E':8, 'G':11},
    'G': {'E':9, 'F':11},
}
# fringe is a collection of nodes reachable but not visited yet
#for bfs: queue

def bfs(graph, start_v):
    visited = list()
    queue = [start_v] #fringe
    while queue: # while queue is not empty
        v = queue.pop(0) # remove front vertex
        visited.append(v) # visit this vertex
        # explore neighbors of v
        for w in graph[v].keys(): # for each neighbor of v
            if w not in visited and w not in queue:
                queue.append(w)
    return visited

# for dfs: stack
def dfs(graph, start_v):
    visited = list()
    stack = [start_v]
    while stack:
        v = stack.pop() # stack pop
        visited.append(v)
        for w in graph[v].keys():
            if w not in visited and w not in stack:
                stack.append(w) # stack push
    return visited

def uniform_cost_search(graph, start_v):
    pq = list() # fringe min priority queue
    visited = list()
    # tuple (path, cost, vertex)
    heapq.heappush(pq, (0, start_v))
    # give dictionary to store path cot of each v
    lookup_dict = {start_v: 0}
    while pq:
        cost, v = heapq.heappop(pq)
        if v not in visited:
            visited.append(v)
            for w, edge_weight in graph[v].items():
                # new weight
                new_weight = cost + edge_weight
                if w not in lookup_dict or new_weight < lookup_dict[w]:
                    lookup_dict[w] = new_weight
                    heapq.heappush(pq, (new_weight, w))
    return visited


print(bfs(graph, 'A'))
print(dfs(graph, 'A'))
print(uniform_cost_search(graph, 'A'))

