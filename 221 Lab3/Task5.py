def qsort(arr,start,finish):
    if start<finish:
        pivot=partition(arr,start,finish)
        qsort(arr,start,pivot-1)
        qsort(arr,pivot+1,finish)

def partition(arr,start,finish):
    pivot=arr[finish]
    i=start-1
    for j in range(start,finish):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[finish]=arr[finish],arr[i+1]
    return i+1

with open('input5.txt','r') as file:
    with open('output5.txt','w') as file2:
        N=int(file.readline())
        M=list(map(int,file.readline().split()))
        qsort(M,0,N-1)
        for i in M:
            file2.write(f'{i} ')