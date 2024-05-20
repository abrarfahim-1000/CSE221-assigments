with open('input1(B).txt', 'r') as fin:
    with open('output1(B).txt','w') as fout:
        ver,edg = list(map(int,fin.readline().split()))
        dic={}
        for _ in range(ver+1):
            dic[_]=[]
        for i in range(edg):
            a=list(map(int,fin.readline().split()))
            tup=tuple(a[1:])
            if a[0] in dic:
                dic[a[0]].append(tup)
            else:
                dic[a[0]]=[tup]
        for i,j in dic.items():
            fout.write(f'{i}:')
            for k in j:
                fout.write(str(k))
            fout.write('\n')