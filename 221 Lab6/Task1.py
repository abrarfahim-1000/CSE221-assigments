import heapq
def dijkstra(graph,start,num_nodes):
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
                distance[neighbor]=min(distance[neighbor],current_distance+weight)
                heapq.heappush(heap,(distance[neighbor],neighbor))
    return distance

with open('input1_2.txt', 'r') as fin:
    with open('output1_2.txt', 'w') as fout:
        var=[line.strip() for line in fin.readlines()]
        node,edge=map(int,var[0].split())
        source=int(var.pop())
        adj=[]
        for i in range(node+1):
            adj.append([])
        for i in range(1,edge+1):
            a,*b=map(int,var[i].split())
            adj[a].append(b)
        final=dijkstra(adj,source,node)
        for i in range(1,len(final)):
            if type(final[i])!=float:
                fout.write(f'{final[i]} ')
            else:
                fout.write(f'{-1} ')