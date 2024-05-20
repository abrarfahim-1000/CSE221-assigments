def occurrence(arr, target):
    left1, right1 = 0, len(arr) - 1
    result1 = -1
    while left1 <= right1:
        mid1 = left1 + (right1 - left1) // 2
        if arr[mid1] == target:
            result1 = mid1
            right1 = mid1 - 1
        elif arr[mid1] < target:
            left1 = mid1 + 1
        else:
            right1 = mid1 - 1

    left2, right2 = 0, len(arr) - 1
    result2 = -1
    while left2 <= right2:
        mid2 = left2 + (right2 - left2) // 2
        if arr[mid2] == target:
            result2 = mid2
            left2 = mid2 + 1
        elif arr[mid2] < target:
            left2 = mid2 + 1
        else:
            right2 = mid2 - 1

    return result2-result1+1
    

# Example usage:
arr = [1, 3, 4, 5, 13, 15, 16, 16, 16, 16, 19, 21, 21, 23]
target = 16
print("Number of occurrences of", target, ":", occurrence(arr, target))  # Output: 4