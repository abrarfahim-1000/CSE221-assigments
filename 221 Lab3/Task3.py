def merge(array):
    i=j=k=inv=0
    if len(array)>1:
        mid=len(array)//2
        left=array[:mid]
        right=array[mid:]
        inv+=merge(left)
        inv+=merge(right)
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
                inv+=len(left)-i
                array[k]=right[j]
                j+=1
                k+=1
            else:
                array[k]=left[i];array[k]=right[j]
                i+=1
                j+=1
                k+=1
    return inv

with open('input3.txt','r') as file:
    with open('output3.txt','w') as file2:
        N=int(file.readline())
        M=list(map(int,file.readline().split()))
        file2.write(str(merge(M)))