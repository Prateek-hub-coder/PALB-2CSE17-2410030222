def smallest_subarray(x, arr):
    n = len(arr)
    min_length = n + 1
    current_sum = 0
    start = 0

    for end in range(n):
        # Add current element
        current_sum += arr[end]
        while current_sum > x:
            length = end - start + 1
            if length < min_length:
                min_length = length
            
            current_sum -= arr[start]
            start += 1

    if min_length == n + 1:
        return 0
    
    return min_length


x = 51
arr = [1, 4, 45, 6, 0, 19]
print(smallest_subarray(x, arr))  
