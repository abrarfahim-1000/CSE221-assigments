def dfs(v,list1,visited,stk):
    visited[v]=True
    for j in list1[v]:
        if not visited[j]:
            dfs(j,list1,visited,stk)
    stk.insert(0,v)

def basedfs(v,list1,visited):
    visited[v]=1
    fout.write(f'{v} ')
    for j in list1[v]:
        if visited[j]==0:
            basedfs(j,list1,visited)

with open('input3_2.txt', 'r') as fin:
    with open('output3_2.txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        adj=[[] for i in range(ver+1)]
        visited=[0]*(ver+1)
        visited1=[0]*(ver+1)
        adjrev=[[] for i in range(ver+1)]
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            adj[a].append(b)
            adjrev[b].append(a)
            stk=[]
        for  i in range(1,ver+1):
                if len(adj[i])==0: continue
                if visited[i]: continue
                dfs(i,adj,visited,stk)
        while stk:
            u=stk.pop(0)
            if not visited1[u]:
                basedfs(u,adjrev,visited1)
                fout.write('\n')