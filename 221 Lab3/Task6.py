def qselect(arr,left,right,k): 
	if k>0 and k<=right-left+1:
		pivot=partition(arr,left,right) 
		if pivot-left==k-1: 
			return arr[pivot] 
		if pivot-left>k-1: 
			return qselect(arr,left,pivot-1,k) 
		return qselect(arr,pivot+1,right,k-pivot+left-1)
	
def partition(arr,start,finish):
    pivot=arr[finish]
    i=start-1
    for j in range(start,finish):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[finish]=arr[finish],arr[i+1]
    return i+1

with open('input6.txt','r') as file:
    with open('output6.txt','w') as file2:
        N=int(file.readline())
        M=list(map(int,file.readline().split()))
        times=int(file.readline())
        for i in range(times):
              k=int(file.readline())
              file2.write(str(qselect(M,0,N-1,k)))
              if i!=times-1:
                    file2.write('\n')
