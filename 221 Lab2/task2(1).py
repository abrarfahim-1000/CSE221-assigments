def merge(array):
    if len(array)>1:
        mid=len(array)//2
        left=array[:mid]
        right=array[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while i<len(left) or j<len(right):
            if i>=len(left):
                array[k]=right[j]
                j+=1
                k+=1
            elif j>=len(right):
                array[k]=left[i]
                i+=1
                k+=1
            elif left[i]<right[j]:
                array[k]=left[i]
                i+=1
                k+=1
            elif left[i]>right[j]:
                array[k]=right[j]
                j+=1
                k+=1
            else:
                array[k]=left[i];array[k]=right[j]
                i+=1
                j+=1
                k+=1

with open('input2.txt','r') as file:
    with open('output2.txt','w') as file2:
        len1=int(file.readline())
        array1=list(map(int,file.readline().split()))
        len2=int(file.readline())
        array2=list(map(int,file.readline().split()))
        i=0;j=0
        for el in array2:
            array1.append(el)
        merge(array1)
        for  el in array1:
            file2.write(f'{el} ')
        file2.write(f'\n')