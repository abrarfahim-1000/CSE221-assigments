with open('input1.txt','r') as file:
    with open('output1.txt','w') as file2:
        length,target=list(map(int,file.readline().split()))
        array=list(map(int,file.readline().split()))
        first=0
        last=length-1
        flag=True
        while first<last:
            if array[first]+array[last]==target:
                file2.write(f'{first+1} {last+1}\n')
                flag=False
                break
            elif array[first]+array[last]<target:
                first+=1
            else:
                last-=1
        if flag:
            file2.write('IMPOSSIBLE\n')