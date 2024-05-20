def union(parent,u,v):
    if u==v:
        parent[v]=u
    else:
        if u<v:
            for i in range(len(parent)):
                if parent[i]==v:
                    parent[i]=u
        else:
            for i in range(len(parent)):
                if parent[i]==u:
                    parent[i]=v

def find(parent,r):
	if parent[r]==r:
		return r
	return find(parent,parent[r])

def kruskal(graph,city):
    graph=sorted(graph,key=lambda edge:edge[2])
    i=0
    mst=[]
    parent=[]
    edge=0
    for node in range(city+1):
        parent.append(node)
    while edge<city-1:
        u,v,cost=graph[i]
        a=find(parent,u)
        b=find(parent,v)
        i+=1
        if a!=b:
            edge+=1
            mst.append([u,v,cost])
            union(parent,a,b)
    final=0
    for u,v,cost in mst:
        final+=cost
    return final

with open ('input2_1.txt','r') as fin:
    with open('output2_1.txt','w') as fout:
        city,road=list(map(int,fin.readline().split()))
        graph=[]
        for i in range(road):
            graph.append(list(map(int,fin.readline().split())))
        fout.write(f'{kruskal(graph,city)}')
        