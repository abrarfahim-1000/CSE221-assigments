import heapq
with open('input3.txt','r') as fin:
    # with open('output1','w') as fout:
        ver,edge=map(int,fin.readline().split())
        graph=[[] for i in range(ver+1)]
        for i in range(edge):
            u,v,w=list(map(int,fin.readline().split()))
            graph[u].append((v,w))
            graph[v].append((u,w))

def dijkstra_all_paths(graph, start):
    num_nodes = len(graph)
    distances = [float('infinity')] * num_nodes
    distances[start] = 0
    paths = [[] for _ in range(num_nodes)]
    paths[start] = [[start]]
    queue = [(0,start)]
    while queue:
        current_distance,current_node = heapq.heappop(queue)
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = [path + [neighbor] for path in paths[current_node]]
                heapq.heappush(queue,(distance,neighbor))
            elif distance == distances[neighbor]:
                paths[neighbor].extend([path + [neighbor] for path in paths[current_node]])
    return distances, paths
start_node = 1
target_node = 5
shortest_distances, all_shortest_paths = dijkstra_all_paths(graph, start_node)

print("Shortest distances to each node:", shortest_distances)
print("All shortest paths to {}: {}".format(target_node, all_shortest_paths[target_node]))
print(min(all_shortest_paths[target_node]))
