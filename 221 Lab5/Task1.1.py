def dfs(v,list1,visited,stk):
    visited[v]=True
    for j in list1[v]:
        if not visited[j]:
            dfs(j,list1,visited,stk)
    stk.insert(0,v)

def cycler(u,list1,visited,path):
    visited[u]=True
    path[u]=True
    cycle=False
    for i in list1[u]:
        if visited[i] and path[i]:
            return True
        else:
            cycle=cycle or cycler(i,list1,visited,path)
    path[u]=False
    return cycle

with open('input1_1.txt', 'r') as fin:
    with open('output1_1.txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        adj=[[] for i in range(ver+1)]
        visited=[False]*(ver+1)
        stk=[]
        visited1=[False]*(ver+1)
        path=[False]*(ver+1)
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            adj[a].append(b)
        for  i in range(1,ver+1):
            if len(adj[i])==0: continue
            if visited[i]: continue
            cycle=cycler(i,adj,visited,path)
        
        if not cycle:
            for  i in range(1,ver+1):
                if len(adj[i])==0: continue
                if visited1[i]: continue
                dfs(i,adj,visited1,stk)
            for i in stk:
                fout.write(str(i)+' ')
        else:
            fout.write('Impossible')