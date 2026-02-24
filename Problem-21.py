def min_chocolate_difference(arr, m):
    # Sort the packets
    arr = sorted(arr)
    
    # Assume first m packets give minimum difference
    min_diff = arr[m - 1] - arr[0]
    
    for i in range(1, len(arr) - m + 1):
        current_diff = arr[i + m - 1] - arr[i]
        
        if current_diff < min_diff:
            min_diff = current_diff
    
    return min_diff


arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

print(min_chocolate_difference(arr, m))
