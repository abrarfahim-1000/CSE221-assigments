def dfs(start,adj,visited):
    visited[start]=True
    for i in adj[start]:
        if visited[i]==False:
            dfs(i,adj,visited)

with open('input3.txt', 'r') as fin:
    with open('output3.txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        list1=[[] for i in range(ver+1)]
        visited=[0]*(ver+1)
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            list1[a].append(b)
            list1[b].append(a)
        for  i in range(1,ver+1):
            if len(list1[i])==0: continue
            if visited[i]!=0: continue
            dfs(i,list1,visited)