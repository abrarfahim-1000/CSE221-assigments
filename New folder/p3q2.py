A=[23, 2, 19, 3, 7, 11, 5]

def agepiche(arr):
    a,b=0,len(arr)-1
    if b%2==0:
        b-=1
    arr2=[0]*len(arr)
    i=0
    while i<len(arr):
        if a>len(arr):
            arr2[i]=arr[b]
            b-=2
        elif b<0:
            arr2[i]=arr[a]
            a+=2
        elif arr[a]<arr[b]:
            arr2[i]=arr[b]
            b-=2
        else:
            arr2[i]=arr[a]
            a+=2
        i+=1
    return arr2
print(agepiche(A))