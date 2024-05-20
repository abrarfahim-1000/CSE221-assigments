import heapq
def danger_dijkstra(graph,start,num_nodes):
    distance=[float('inf')]*(num_nodes+1)
    distance[start]=0
    visited=[False]*(num_nodes+1)
    heap=[(0, start)]
    while heap:
        current_distance,current_node=heapq.heappop(heap)
        if visited[current_node]:
            continue
        visited[current_node]=True
        for neighbor,weight in graph[current_node]:
            if not visited[neighbor]:
                distance[neighbor]=min(distance[neighbor],max(current_distance,weight))
                heapq.heappush(heap,(distance[neighbor],neighbor))
    return distance

with open('input3_2.txt', 'r') as fin:
    with open('output3_2.txt', 'w') as fout:
        var=[line.strip() for line in fin.readlines()]
        node,edge=list(map(int,var.pop(0).split()))
        adj=[]
        for i in range(node+1):
            adj.append([])
        for i in range(len(var)):
            a,*b=map(int,var[i].split())
            adj[a].append(b)
        fout.write(f'{danger_dijkstra(adj,1,node)[node]}')
