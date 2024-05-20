def bfs(i,adj,visited,queue,parent):
    parent[i]=-1
    queue.append(i)
    while len(queue)>0:
        u=queue.pop(0)
        visited[u]=1
        for v in adj[u]:
            if visited[v]==0:
                parent[v]=u
                visited[v]=1
                queue.append(v)

def pathcheck(target,parent):
    temp=target
    path=[]
    while True:
        path=[temp]+path
        temp=parent[temp]
        if temp==-1:
            break
    return path

with open('input5.txt', 'r') as fin:
    with open('output5.txt','w') as fout:
        ver,edg,target = list(map(int,fin.readline().split()))
        list1=[[] for i in range(ver+1)]
        visited=[0]*(ver+1)
        parent=[0]*(ver+1)
        queue=[]
        for i in range(edg):
            a,b=map(int,fin.readline().split())
            list1[a].append(b)
            list1[b].append(a)
  
        for i in range(1,ver+1):
            if len(list1[i])==0: continue
            if visited[i]!=0: continue
            bfs(i,list1,visited,queue,parent)
   
        for i in pathcheck(target,parent):
            fout.write(f'{i} ')