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

A=[1, 3, 4, 5, 9, 6, 2, -1]
merge(A)
print(A[len(A)-1])