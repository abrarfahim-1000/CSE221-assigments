def maxcrossarray(arr,k):
    leftsum=0
    for i in range(k,-1,-1):
        if arr[i]=='0':
            leftsum+=1
        else:
            break
    rightsum=0
    for i in range(k+1,len(arr)):
        if arr[i]=='0':
            rightsum+=1
        else:
            break
    return max(leftsum,rightsum,leftsum+rightsum)

def maxsubarray(arr):
    if len(arr)==1:
        if arr[0]=="1":
            return 0
        else:
            return 1
    mid=len(arr)//2
    return max(maxsubarray(arr[:mid]),maxsubarray(arr[mid:]),maxcrossarray(arr,mid))

arr='10000000000000100000111'
print(maxsubarray(arr))