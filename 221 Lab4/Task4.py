def cycler(start,adj,visited,path):
    visited[start]=True
    path[start]=True
    cycle=False
    for i in adj[start]:
        if visited[i] and path[i]:
            return True
        else:
            cycle=cycle or cycler(i,adj,visited,path)
    path[start]=False
    return cycle

with open('input4.txt', 'r') as fin:
    with open('output4.txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        list1=[[] for i in range(ver+1)]
        visited=[False]*(ver+1)
        path=[False]*(ver+1)
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            list1[a].append(b)
        for  i in range(1,ver+1):
            if len(list1[i])==0: continue
            if visited[i]!=0: continue
            if cycler(i,list1,visited,path):
                fout.write('yes')
            else:
                fout.write('no')