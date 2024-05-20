def findmax(arr):
    if len(arr)==1:
        return arr[0]
    mid=len(arr)//2
    left=findmax(arr[:mid])
    right=findmax(arr[mid:])
    if left>right:
        return left
    else:
        return right
    
with open('input2.txt','r') as file:
    with open('output2.txt','w') as file2:
        N=int(file.readline())
        M=list(map(int,file.readline().split()))
        file2.write(str(findmax(M)))