def bfs(start,adj,visited,queue):
    queue.append(start)
    while len(queue)>0:
        u=queue.pop(0)
        if not visited[u]:
            print(u)
            visited[u]=True
            for v in adj[u]:
                if not visited[v]:
                    queue.append(v)


with open('input2.txt', 'r') as fin:
    with open('output2.txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        list1=[[] for i in range(ver+1)]
        visited=[0]*(ver+1)
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            list1[a].append(b)
            list1[b].append(a)
        queue=[]
        for i in range(1,ver+1):
            if len(list1[i])==0: continue
            if visited[i]!=0: continue
            bfs(i,list1,visited,queue)
