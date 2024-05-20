import numpy
def matrix(ver,graph):
    mat=numpy.full((ver+1,ver+1),0)
    for i in graph:
        mat[i[0]][i[1]]=i[2]
    return mat

with open('input1(A).txt', 'r') as fin:
    with open('output1(A).txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        list1=[]
        for i in range(edg):
            a,b,c=list(map(int,fin.readline().split()))
            list1.append([a,b,c])
        mat=matrix(ver,list1)
        for i in range(ver+1):
            for j in range(ver+1):
                fout.write(str(mat[i][j]))
            fout.write('\n')