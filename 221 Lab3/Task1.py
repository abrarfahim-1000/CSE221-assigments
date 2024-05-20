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

with open('input1.txt','r') as file:
    with open('output1.txt','w') as file2:
        N=int(file.readline())
        M=list(map(int,file.readline().split()))
        merge(M)
        for i in M:
            file2.write(f'{i} ')