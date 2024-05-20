def modified_count_sort(arr):
    min_val = int(min(arr)*10)
    max_val = int(max(arr)*10)
    rang=max_val-min_val
    count = [0] * (rang+1)
    for num in arr:
        count[int(num*10) - min_val] += 1
    output=[]
    for i in range(len(count)):
        for j in range(count[i]):
            output.append(((i+min_val)/10))
    return output

A= [2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2]

print("Given array is", A)
print("\nSorted array is", modified_count_sort(A))