import heapq
def dijk(start,adj,n):
    visited=[False]*(n+1)
    dist=[0]*(n+1)
    queue=[(1,start)]
    dist[start]=1
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        if visited[current_node]:
            continue
        visited[current_node]=True
        
        for neighbor,weight in adj[current_node]:

            dist[neighbor]=max(dist[neighbor],weight*current_distance)
            heapq.heappush(queue,(dist[neighbor],neighbor))
    return dist

with open('input2.txt','r') as fin:
    # with open('output2','w') as fout:
        ver,edge=map(int,fin.readline().split())
        adj=[[] for i in range(ver)]
        for i in range(edge):
            var=fin.readline().strip().split()
            a=int(var[0]);b=int(var[1]);c=float(var[2])
            # print(a,b,c)
            adj[a].append((b,c))
            # adj[b].append((a,c))
        print(adj)
        print(dijk(0,adj,ver))