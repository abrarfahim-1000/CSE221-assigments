def modified_count_sort(arr):
    min_val = int(min(arr))
    max_val = int(max(arr))
    rang=max_val-min_val
    count = [0] * (rang+1)
    for num in arr:
        count[num - min_val] += 1
    output=[]
    for i in range(len(count)):
        for j in range(count[i]):
            output.append((i+min_val))
    return output

# A= [2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2]
A=[1, 3, 4, 5, 6, 2, -1,9]
print("Given array is", A)
print("\nSorted array is", modified_count_sort(A))

