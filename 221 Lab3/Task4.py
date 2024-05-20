def maxval(arr):
    if len(arr)==1: 
        return arr[0]
    else:
        mid=len(arr)//2
        left=maxval(arr[:mid])
        right=maxval(arr[mid:])
        if left>right:
            return left
        return right
    
def maxvalsq(arr):
    if len(arr)==1:
        return arr[0]**2
    else:
        mid=len(arr)//2
        lmax=maxvalsq(arr[:mid])
        rmax=maxvalsq(arr[mid:])
        if lmax>rmax:
             return lmax
        return rmax
    
def answer(arr):
    if len(arr)==1:
        return arr[0]
    else:
        mid=len(arr)//2
        left=answer(arr[:mid])
        right=answer(arr[mid:])
        temp=maxval(arr[:mid])+maxvalsq(arr[mid:])
        return max(left,right,temp)
    
with open('input4.txt','r') as file:
    with open('output4.txt','w') as file2:
        N=int(file.readline())
        M=list(map(int,file.readline().split()))
        file2.write(str(answer(M)))