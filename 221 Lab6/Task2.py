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

with open('input2_3.txt', 'r') as fin:
    with open('output2_3.txt', 'w') as fout:
        var=[line.strip() for line in fin.readlines()]
        node,edge=map(int,var[0].split())
        player1,player2=map(int,var[len(var)-1].split())
        adj=[]
        for i in range(node+1):
            adj.append([])
        for i in range(1,edge+1):
            a,*b=map(int,var[i].split())
            adj[a].append(b)
        p1=dijkstra(adj,player1,node);p1.pop(0)
        p2=dijkstra(adj,player2,node);p2.pop(0)
        mintime=float('inf')
        time,n=0,0
        for i in range(node):
             if (p1[i]!=0 and type(p1[i])!=float) and (p2[i]!=0 and type(p2[i])!=float):
                if max(p1[i],p2[i])<mintime:
                    time=max(p1[i],p2[i])
                    n=i+1
                    mintime=time
        if time==0 and n==0:
            fout.write('Impossible')
        else:
            fout.write(f'Time: {time}\nNode: {n}')