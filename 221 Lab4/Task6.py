import numpy
path=[(0,-1),(-1,0),(1,0),(0,1)]
with open('input6.txt', 'r') as fin:
    with open('output6.txt','w') as fout:
        row,col=list(map(int,fin.readline().split()))
        mat=numpy.full((row,col),None)
        visited=numpy.full((row,col),None)
        queue=[]
        counter=[]
        for i in  range(row):
            line=fin.readline()
            for j in range(col):
                mat[i][j]=line[j]
        def valid(x,y):
            if -1<x<row and -1<y<col:
                if mat[x][y]=='#':
                    return False
                else:
                    return True
            else :
                return False

        def bfs(i,j,mat,visited,queue):
            queue.append((i,j))
            visited[i][j]=True
            count=0
            while len(queue)>0:
                u=queue.pop(0)
                i=u[0]
                j=u[1]
                if mat[i][j]=='D':
                    count+=1       
                for el in path:
                    ni=u[0]+el[0]
                    nj=u[1]+el[1]
                    if valid(ni,nj):
                        if not visited[ni][nj]:
                            queue.append((ni,nj))
                            visited[ni][nj]=True
            counter.append(count)
        
        for i in range(row):
            for j in range(col):
                if mat[i][j]=='#': continue
                if visited[i][j]: continue
                bfs(i,j,mat,visited,queue)
        fout.write(f'{max(counter)}')