with open('input2.txt','r') as file:
    with open('output2.txt','w') as file2:
        len1=int(file.readline())
        array1=list(map(int,file.readline().split()))
        len2=int(file.readline())
        array2=list(map(int,file.readline().split()))
        final=[]
        i=0;j=0
        while i<len1 or j<len2:
            if i>=len1:
                final.append(array2[j])
                j+=1
            elif j>=len2:
                final.append(array1[i])
                i+=1
            elif array1[i]<array2[j]:
                final.append(array1[i])
                i+=1
            elif array1[i]>array2[j]:
                final.append(array2[j])
                j+=1
            else:
                final.append(array1[i]);final.append(array2[j])
                i+=1
                j+=1
        for num in final:
            file2.write(f'{num} ')
        file2.write('\n')