with open('input1.txt','r') as file:
    with open('output1.txt','w') as file2: 
        length,target=list(map(int,file.readline().split()))
        array=list(map(int,file.readline().split()))
        flag=False
        flag2=False
        count=0
        for i in range(length):
            for j in range(i+1,length):
                if array[i]+array[j]==target:
                    file2.write(f'{i+1} {j+1}\n')
                    flag2=True
                    flag=True
            if flag:    
                break
        if not flag2:
            file2.write('IMPOSSIBLE\n')