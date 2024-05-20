def greedy(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i][0]+array[i][1]>array[j][0]+array[j][1]:
                array[i],array[j]=array[j],array[i]
    sorted=[array[0]]
    endtime=array[0][1]
    for elem in array[1:]:
        start,end=elem
        if start>=endtime:
            sorted.append(elem)
            endtime=end
    return sorted

with open('input3.txt','r') as file:
    with open('output3.txt','w') as file2:
        time=int(file.readline())
        tasklist=[]
        for line in file:
            tasklist.append(list(map(int,line.split())))
        final=greedy(tasklist)
        file2.write(f'{len(final)}\n')
        for tup in final:
            file2.write(f'{str(tup[0])} {str(tup[1])}\n')