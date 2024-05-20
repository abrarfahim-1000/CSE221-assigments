def find(r):
	if parent[r]==r:
		return r
	return find(parent[r])

def union(a,b):
    u=find(a)
    v=find(b)
    if u==v:
        return u
    else:
        if u<v:
            for i in range(len(parent)):
                if parent[i]==v:
                    parent[i]=u
            return u
        else:
            for i in range(len(parent)):
                if parent[i]==u:
                    parent[i]=v
            return v

def setsize(num,parent,sizearray):
    count=0
    for i in range(len(parent)):
        if parent[i]==num:
            count+=1
    sizearray[num]=count
    return sizearray[size]

with open ('input1_1.txt','r') as fin:
    with open('output1_1.txt','w') as fout:
        people,query=list(map(int,fin.readline().split()))
        sizearray=[None]*(people+1)
        for i in range(people+1):
            sizearray[i]=1
        parent=[None]*(people+1)
        for i in range(people+1):
            parent[i]=i
        for i in range(query):
            a,b=list(map(int,fin.readline().split()))
            size=union(a,b)
            fout.write(f'{setsize(size,parent,sizearray)}\n')