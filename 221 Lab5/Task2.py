import heapq
def lexi_kahn(adj, ver):
    priority_queue=[]
    result=[]
    indeg=[0]*(ver+1)
    for i in adj:
        for j in i:
            indeg[j]+=1
    for i in range(1,ver+1):
        if indeg[i]==0:
            heapq.heappush(priority_queue,i)
    while priority_queue:
        u=heapq.heappop(priority_queue)
        result.append(u)
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                heapq.heappush(priority_queue,v)
    return result

with open('input2_3.txt','r') as fin:
    with open('output2_3.txt','w') as fout:
        ver,edg=list(map(int,fin.readline().split()))
        adj=[[] for i in range(ver+1)]
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            adj[a].append(b)
        res=lexi_kahn(adj, ver)
        if len(res)==ver:
            for i in res:
                fout.write(f'{i} ')
        else:
            fout.write('Impossible')