def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        flag=False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag=True
        if not flag:
            break
    return arr
# I have added a flag that acts as an indicator whether there is any swap in the first outer loop iteration. 
# If there is no swap in the first outer loop iteration, then the array is already sorted. 
# Thus the loop can break early, running 1 time instead of n times.


with open ('input2.txt','r') as file:
    with open ('output2.txt','w') as file2:
        time=int(file.readline())
        for i in range (time):
            n=int(file.readline())
            array=(file.readline()).split()
            array=list(map(int,array))
            final=bubbleSort(array)
            for j in range(n):
                file2.write(f'{final[j]} ')
            if i<time-1:
                file2.write('\n')