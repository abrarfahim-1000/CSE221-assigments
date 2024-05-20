import heapq
def ascending_kahn(adj,ver):
    indeg=[0]*(ver)
    queue=[]
    result=[]
    for i in adj:
        for j in i:
            indeg[j]+=1
    for i in range(ver):
        if indeg[i]==0:
            heapq.heappush(queue,(-1*i))
    while queue:
        cur=heapq.heappop(queue)
        current=-1*cur
        result.append(current)
        for i in adj[current]:
            indeg[i]-=1
            if indeg[i]==0:
                heapq.heappush(queue,(-1*i))
    return result

with open('input1.txt','r') as fin:
    # with open('output1','w') as fout:
        ver,edge=map(int,fin.readline().split())
        u=list(map(int,fin.readline().split()))
        v=list(map(int,fin.readline().split()))
        adj=[[] for i in range(ver+1)]
        for i in range(edge):
            adj[u[i]].append(v[i])
        print(ver,edge,adj)
        queue=ascending_kahn(adj,ver)
        if len(queue)!=ver:
            print('yes')
        else:
            print('no')
        print(queue)