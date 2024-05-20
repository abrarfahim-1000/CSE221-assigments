def max_consecutive_zeros(binary_string):
    # Base case: If the string has only one character, return 1 if it's '0' else return 0
    if len(binary_string) == 1:
        return 1 if binary_string == '0' else 0

    # Divide the string into two halves
    mid = len(binary_string) // 2
    left_half = binary_string[:mid]
    right_half = binary_string[mid:]

    # Recursively find the maximum consecutive zeros in each half
    max_consecutive_left = max_consecutive_zeros(left_half)
    max_consecutive_right = max_consecutive_zeros(right_half)

    # Check if there are any consecutive zeros crossing the midpoint
    max_crossing = 0
    consecutive_zeros = 0
    for bit in reversed(left_half):  # Check from right to left in the left half
        if bit == '0':
            consecutive_zeros += 1
            max_crossing = max(max_crossing, consecutive_zeros)
        else:
            consecutive_zeros = 0

    consecutive_zeros = 0
    for bit in right_half:  # Check from left to right in the right half
        if bit == '0':
            consecutive_zeros += 1
            max_crossing = max(max_crossing, consecutive_zeros)
        else:
            consecutive_zeros = 0

    # Return the maximum of the three values: max from left half, max from right half, and max crossing the midpoint
    return max(max_consecutive_left, max_consecutive_right, max_crossing)