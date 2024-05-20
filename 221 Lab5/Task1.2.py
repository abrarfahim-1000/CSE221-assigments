def kahn(adj,ver):
    indeg=[0]*(ver+1)
    queue=[]
    result=[]
    for i in adj:
        for j in i:
            indeg[j]+=1
    for i in range(1,len(indeg)):
        if indeg[i]==0:
            queue.append(i)
    while queue:
        u=queue.pop(0)
        result.append(u)
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                queue.append(v)
    return result

with open('input1_2.txt', 'r') as fin:
    with open('output1_2.txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        adj=[[] for i in range(ver+1)]
        adjrev=[[] for i in range(ver+1)]
        visited=[False]*(ver+1)
        stk=[]
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            adj[a].append(b)
        res=kahn(adj,ver)
        if len(res)==ver:
            for i in res:
                fout.write(f'{i} ')
        else:
            fout.write('Impossible')